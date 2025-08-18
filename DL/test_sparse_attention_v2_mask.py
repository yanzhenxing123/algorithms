import tensorflow as tf
from tensorflow.keras.layers import Dense
import numpy as np
from sparse_tensor_2d import construct_test_qkv
from sparse_attention_v2_with_mask import sparse_multihead_attention_fast_v2
from sparse_attention_for_loop_with_mask import for_loop_dense_mha_with_mask, vectorized_dense_mha_with_mask
import random
import time


# 封装重复逻辑
def fill_array(target_array, source_data, valid_q_ids, valid_k_ids, sparse_q_indices, sparse_k_indices, H_):
    P, _ = source_data.shape
    for p in range(P):
        qid = valid_q_ids[p]
        kid = valid_k_ids[p]
        b = sparse_q_indices[qid, 0]
        f = sparse_q_indices[qid, 1]
        t = sparse_k_indices[kid, 1]
        for h in range(H_):
            target_array[b, h, f, t] = source_data[p, h]
    return target_array


def compare_sparse_and_dense_attention():
    D_1 = 16
    V_1 = 16

    D = 64
    V = 64
    H = 4
    # F = random.randint(50, 100)  # Q len
    F = 1  # target attention
    T = random.randint(1000, 10000)  # KV len

    # T = 1
    B = 16

    print(f"D: {D}, V: {V}, H: {H}, F: {F}, T: {T}, B: {B}")

    # 固定随机种子，保证dense/sparse一致
    seed = 42

    tf.random.set_seed(seed)
    Q_dense, K_dense, V_dense = construct_test_qkv(D_1, V_1, H, F, T, B, output_sparse=False)
    tf.random.set_seed(seed)
    sparse_Q, sparse_K, sparse_V = construct_test_qkv(V_1, V_1, H, F, T, B, output_sparse=True)
    Q_tmp = sparse_Q.to_dense()
    K_tmp = sparse_K.to_dense()
    V_tmp = sparse_V.to_dense()

    dense_layer_Q = Dense(H * D // H, use_bias=False)  # 用于 Q 的映射
    dense_layer_K = Dense(H * D // H, use_bias=False)  # 用于 K 的映射
    dense_layer_V = Dense(H * V // H, use_bias=False)  # 用于 V 的映射

    # 随机生成 mask
    mask_dense = np.random.randint(0, 2, size=(B, F, T))
    # mask_dense = None

    # 1. for循环dense MHA
    start = time.time()
    dense_res = vectorized_dense_mha_with_mask(Q_dense.numpy(), K_dense.numpy(), V_dense.numpy(),
                                               num_heads=H,
                                               size_per_head=D // H,
                                               v_size_per_head=V // H,
                                               mask=mask_dense,
                                               layers=[dense_layer_Q, dense_layer_K, dense_layer_V])
    end = time.time()
    print(f'vectorized_dense_mha_with_mask cost:{end - start:.2f}')

    start = time.time()

    # 2. 稀疏MHA（返回中间结果）
    sparse_res = sparse_multihead_attention_fast_v2(sparse_Q, sparse_K, sparse_V,
                                                    num_heads=H,
                                                    size_per_head=D // H,
                                                    v_size_per_head=V // H,
                                                    mask=mask_dense,
                                                    layers=[dense_layer_Q, dense_layer_K, dense_layer_V])

    end = time.time()
    print(f'sparse_multihead_attention_fast_v2 cost:{end - start:.2f}')

    # 3. 对齐shape（只对非零Q位置对比）
    sparse_indices = sparse_Q.indices.numpy()
    B_idx = sparse_indices[:, 0]
    F_idx = sparse_indices[:, 1]
    dense_scores = dense_res['scores']
    dense_attn = dense_res['attn']
    dense_output = dense_res['output']

    sparse_scores = sparse_res['raw_scores'].numpy()  # [Nq, H]
    sparse_attn = sparse_res['scores'].numpy()  # [Nq, H]
    sparse_output = sparse_res['output'].numpy()  # [Nq, H*V//H]

    raw_scores = sparse_res['raw_scores'].numpy()  # [P, H]
    q_batch_ids = sparse_res['q_batch_ids'].numpy()  # [Nq]
    valid_q_ids = sparse_res['valid_q_ids'].numpy()  # [P]
    valid_k_ids = sparse_res['valid_k_ids'].numpy()  # [P]

    full_scores = np.zeros((B, H, F, T), dtype=np.float32)
    sparse_q_indices = sparse_Q.indices.numpy()  # [Nq, 2]
    sparse_k_indices = sparse_K.indices.numpy()  # [Nk, 2]
    P, H_ = raw_scores.shape

    full_scores = fill_array(full_scores, raw_scores, valid_q_ids, valid_k_ids, sparse_q_indices, sparse_k_indices, H_)

    softmax_scores = sparse_res['scores'].numpy()
    full_attn = np.zeros((B, H, F, T), dtype=np.float32)
    full_attn = fill_array(full_attn, softmax_scores, valid_q_ids, valid_k_ids, sparse_q_indices, sparse_k_indices, H_)

    # 4. 打印对比结果
    print("=== 点积分数(scores) ===")
    diffs = []
    for idx, (q, k) in enumerate(zip(B_idx, F_idx)):
        for h in range(H):
            diffs.append(dense_scores[q, h, k, :] - full_scores[q, h, k, :])

    score_l2_diff = np.linalg.norm(diffs)
    print("L2差:", score_l2_diff)

    print("=== softmax分数(attn) ===")
    attn_l2_diff = np.linalg.norm(dense_attn - full_attn)
    print("L2差:", attn_l2_diff)

    print("=== 输出(output) ===")
    Nq = sparse_indices.shape[0]
    full_sparse_output = np.zeros((B, F, V), dtype=np.float32)
    for i in range(Nq):
        b = sparse_indices[i, 0]
        f = sparse_indices[i, 1]
        if sparse_output[i].shape[0] != V:
            raise ValueError(f"sparse_output[{i}] 形状不匹配，期望长度为 {V}，实际为 {sparse_output[i].shape[0]}")
        full_sparse_output[b, f, :] = sparse_output[i]
    output_l2_diff = np.linalg.norm(dense_output - full_sparse_output)
    print("L2差:", output_l2_diff)

    return score_l2_diff, attn_l2_diff, output_l2_diff


def test_time_cost():
    D_1 = 16
    V_1 = 16
    # # 固定参数
    D = 32 * 4 * 3  # QK embedding dim
    V = 32 * 4 * 3  # V embedding dim
    H = 4  # num heads
    F = 1  # Q len
    T = 4000  # KV len
    B = 2048  # batch size

    print(f"D: {D}, V: {V}, H: {H}, F: {F}, T: {T}, B: {B}")

    # 固定随机种子，保证dense/sparse一致
    seed = 42

    tf.random.set_seed(seed)
    Q_dense, K_dense, V_dense = construct_test_qkv(D_1, V_1, H, F, T, B, output_sparse=False)
    tf.random.set_seed(seed)
    sparse_Q, sparse_K, sparse_V = construct_test_qkv(V_1, V_1, H, F, T, B, output_sparse=True)
    Q_tmp = sparse_Q.to_dense()
    K_tmp = sparse_K.to_dense()
    V_tmp = sparse_V.to_dense()

    dense_layer_Q = Dense(H * D // H, use_bias=False)  # 用于 Q 的映射
    dense_layer_K = Dense(H * D // H, use_bias=False)  # 用于 K 的映射
    dense_layer_V = Dense(H * V // H, use_bias=False)  # 用于 V 的映射

    # 随机生成 mask
    # mask_dense = np.random.randint(0, 2, size=(B, F, T))
    mask_dense = None

    # 1. for循环dense MHA
    start = time.time()
    dense_res = vectorized_dense_mha_with_mask(Q_dense.numpy(), K_dense.numpy(), V_dense.numpy(),
                                               num_heads=H,
                                               size_per_head=D // H,
                                               v_size_per_head=V // H,
                                               mask=mask_dense,
                                               layers=[dense_layer_Q, dense_layer_K, dense_layer_V])
    end = time.time()
    dense_cost = end - start
    print(f'vectorized_dense_mha_with_mask cost:{end - start:.2f}')

    start = time.time()

    # 2. 稀疏MHA（返回中间结果）
    sparse_res = sparse_multihead_attention_fast_v2(sparse_Q, sparse_K, sparse_V,
                                                    num_heads=H,
                                                    size_per_head=D // H,
                                                    v_size_per_head=V // H,
                                                    mask=mask_dense,
                                                    layers=[dense_layer_Q, dense_layer_K, dense_layer_V])

    end = time.time()
    sparse_cost = end - start
    print(f'sparse_multihead_attention_fast_v2 cost:{end - start:.2f}')
    return dense_cost, sparse_cost


def test_acc():
    num_tests = 21
    for i in range(num_tests):
        print(f"\n--- 测试 {i + 1} ---")
        compare_sparse_and_dense_attention()


def test_time():
    num_tests = 21
    dense_cost_li = []
    sparse_cost_li = []

    for i in range(num_tests):
        print(f"\n--- 测试 {i + 1} ---")
        dense_cost, sparse_cost = test_time_cost()
        dense_cost_li.append(dense_cost)
        sparse_cost_li.append(sparse_cost)
    print(f"dense_cost_li.mean: {np.mean(dense_cost_li[1:])}")
    print(f"sparse_cost_li.mean: {np.mean(sparse_cost_li[1:])}")


def test_gpu_usage(B, H, F, T, D, V):
    print(f"F:{F}, T: {T}")
    D_h = D // H
    V_h = V // H
    dense = B * H * (F * D_h + T * D_h + F * T + F * V_h) * 4
    if F == 1:
        alpha = 0.33
    else:
        alpha = 0.12
    P = B * F * T * alpha
    sparse = P * H * (2 * D_h + V_h) * 4
    print(f"dense: {dense}")
    print(f"sparse: {sparse}")


def main():
    # test_acc()
    test_time()
    # test_gpu_usage(B=512, H=4, F=100, T=100, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=300, T=300, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=500, T=500, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=1000, T=1000, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=5000, T=5000, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=10000, T=10000, D=64, V=64)
    #
    # test_gpu_usage(B=512, H=4, F=1, T=100, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=1, T=300, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=1, T=500, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=1, T=1000, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=1, T=5000, D=64, V=64)
    # test_gpu_usage(B=512, H=4, F=1, T=10000, D=64, V=64)


if __name__ == '__main__':
    main()
