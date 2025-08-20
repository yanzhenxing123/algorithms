import tensorflow as tf
import numpy as np
from sparse_tensor_2d import construct_test_qkv
from sparse_tensor_2d import SparseTensor2dValue
import random

# 设置随机种子
tf.random.set_seed(42)  # 设置 TensorFlow 的随机种子
np.random.seed(42)  # 设置 NumPy 的随机种子
random.seed(42)  # 设置 Python 的随机种子

"""
不使用 map_fn 的向量化稀疏多头注意力实现。

Args:
    query_sparse: SparseTensor, shape = [B, F, D]
    key_sparse: SparseTensor, shape = [B, T, D]
    value_sparse: SparseTensor, shape = [B, T, V]
    num_heads: int
    size_per_head: int (D = num_heads * size_per_head)
    v_size_per_head: Optional[int] (如果 V != D)

Returns:
    merged_context: Tensor, shape = [Nq, num_heads * v_size_per_head]



q_indices： array([[0, 0],
               [0, 1],
               [2, 0],
               [2, 1]])> dense_shape = [4, 2, 8]
[x, x]
[_, _]
[x, x]
[_, _]
q_values: array([[0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
           [1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7],
           [2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7],
           [3. , 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7]], dtype=float32)>

q_batch_ids = [0, 0, 2, 2]



k_indices  array([[0, 1],
               [0, 2],
               [1, 0],
               [2, 3],
               [3, 1]])> dense_shape = [4, 4, 8]

[_, x, x, _]
[x, _, _, _]
[_, _, _, x]
[_, x, _, _]
array([[0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
   [1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7],
   [2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7],
   [3. , 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7],
   [4., 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7]], dtype=float32)>
k_batch_ids = [0, 0, 1, 2, 3]

batch_eq_mask = tf.equal(
    tf.expand_dims(q_batch_ids, axis=1),  # [4, 1] 里面的值表示batch中的行
    tf.expand_dims(k_batch_ids, axis=0)  # [1, 5] 里面的值表示batch中的行
) = array([[ True,  True, False, False, False],
       [ True,  True, False, False, False],
       [False, False, False,  True, False],
       [False, False, False,  True, False]])> # q和k的每个向量是否在同一个batch


valid_indices = tf.where(batch_eq_mask) # 取 batch_eq_mask 为true的索引
        = array([[0, 0],
               [0, 1],
               [1, 0],
               [1, 1],
               [2, 3],
               [3, 3]])>

valid_q_ids = valid_indices[:, 0]  = [0, 0, 1, 1, 2, 3] # 每个元素表示的就是第几个
valid_k_ids = valid_indices[:, 1]  = [0, 1, 0, 1, 3, 3] # 获取第二个索引列作为 valid_k_ids

# 没啥好说的
query_layer = tf.reshape(q_values, [-1, num_heads, size_per_head])  # [Nq, H, D] TensorShape([4, 2, 4])
key_layer = tf.reshape(k_values, [-1, num_heads, size_per_head])  # [Nk, H, D] TensorShape([5, 2, 4])
value_layer = tf.reshape(v_values, [-1, num_heads, v_size_per_head])  # [Nv, H, V] TensorShape([5, 2, 4])

# 选取这里的元素
selected_q = tf.gather(query_layer, valid_q_ids)  # [P, H, D]
selected_k = tf.gather(key_layer, valid_k_ids)  # [P, H, D]






    if tf.size(k_values) == 0 or tf.size(v_values) == 0:
        print("Warning: Empty key or value sequence detected, returning default values.")
        # 将 scores 和 output 设为全 0 或默认值
        scores = tf.zeros([tf.shape(q_values)[0], num_heads], dtype=tf.float32)  # [Nq, H]
        merged_context = tf.zeros([tf.shape(q_values)[0], num_heads * v_size_per_head], dtype=tf.float32)  # [Nq, H*V_h]
        return {
            'scores': scores,
            'raw_scores': scores,
            'output': merged_context,
            'q_batch_ids': q_indices[:, 0],  # [Nq]
            'valid_q_ids': tf.zeros_like(q_indices[:, 0], dtype=tf.int32),  # [Nq] 为空的情况，valid_q_ids 为空
            'valid_k_ids': tf.zeros_like(k_indices[:, 0], dtype=tf.int32),  # [Nk] 为空的情况，valid_k_ids 为空
        }

"""


def get_valid_indices(batch_eq_mask):
    """
    通过分块处理的方式获取 batch_eq_mask 中为 True 的有效索引。

    Args:
        batch_eq_mask (tf.Tensor): 形状为 [Nq, Nk] 的布尔张量。
        chunk_size (int, optional): 分块处理的块大小，默认为 1024。

    Returns:
        tf.Tensor: 有效索引，形状为 [P, 2]。
    """

    Nq = batch_eq_mask.shape[0]
    Nk = batch_eq_mask.shape[1]

    max_value = 2 ** 30
    chunk_size = max(max(0, 1 << (max_value // Nk).bit_length() - 1), 1)

    # chunk_size = 2
    print(f"chunk_size: {chunk_size}")
    all_valid_indices = []

    for i in range(0, Nq, chunk_size):
        end = min(i + chunk_size, Nq)
        chunk_mask = batch_eq_mask[i:end]
        # 1024 * 10000
        chunk_valid_indices = tf.where(chunk_mask)
        # 调整索引偏移量
        chunk_valid_indices = chunk_valid_indices + [i, 0]
        all_valid_indices.append(chunk_valid_indices)

    valid_indices = tf.concat(all_valid_indices, axis=0)
    return valid_indices


def get_valid_indices_v2(q_batch_ids, k_batch_ids):
    from collections import defaultdict
    import itertools
    a = q_batch_ids.numpy()
    b = k_batch_ids.numpy()

    # 步骤1：记录每个值在a和b中的索引位置
    a_indices = defaultdict(list)
    b_indices = defaultdict(list)

    # 使用列表推导式记录索引
    _ = [a_indices[num].append(idx) for idx, num in enumerate(a)]
    _ = [b_indices[num].append(idx) for idx, num in enumerate(b)]

    # 步骤2：对共同元素生成索引笛卡尔积
    common_values = sorted(set(a_indices.keys()) & set(b_indices.keys()))

    # 使用 map 和 itertools.chain 生成结果
    from itertools import chain
    result_pairs = list(chain(*map(lambda v: itertools.product(a_indices[v], b_indices[v]), common_values)))

    # 将结果转换为 TensorFlow 的 Tensor
    result_tensor = tf.constant(result_pairs, dtype=tf.int32)

    return result_tensor


def sparse_multihead_attention_fast_v2(query_sparse,
                                       key_sparse,
                                       value_sparse,
                                       num_heads,
                                       size_per_head,
                                       v_size_per_head=None,
                                       mask=None,
                                       layers=[]
                                       ):
    if v_size_per_head is None:
        v_size_per_head = size_per_head
    is_mhta = query_sparse.dense_shape[1] == 1

    B = query_sparse.dense_shape[0]
    F = query_sparse.dense_shape[1]
    T = key_sparse.dense_shape[1]

    # 统一索引类型
    q_indices, q_values = query_sparse.indices, query_sparse.values  # [Nq, 2], [Nq, D]
    k_indices, k_values = key_sparse.indices, key_sparse.values  # [Nk, 2], [Nk, D]
    v_values = value_sparse.values  # [Nv, V]

    if layers:  # 测试使用
        dense_layer_Q, dense_layer_K, dense_layer_V = layers
    else:
        dense_layer_Q = tf.keras.layers.Dense(num_heads * size_per_head, use_bias=False)  # 用于 Q 的映射
        dense_layer_K = tf.keras.layers.Dense(num_heads * size_per_head, use_bias=False)  # 用于 K 的映射
        dense_layer_V = tf.keras.layers.Dense(num_heads * v_size_per_head, use_bias=False)  # 用于 V 的映射


    # 对 Q/K/V 进行映射
    q_values = dense_layer_Q(q_values)  # [B, F, D] -> [B, F, H * D_h]
    k_values = dense_layer_K(k_values)  # [B, T, D] -> [B, T, H * D_h]
    v_values = dense_layer_V(v_values)  # [B, T, V] -> [B, T, H * V_h]

    q_batch_ids = tf.cast(q_indices[:, 0], tf.int32)
    k_batch_ids = tf.cast(k_indices[:, 0], tf.int32)

    # batch对齐
    # 第一种方法拿到 valid_indices
    # batch_eq_mask = tf.equal(tf.expand_dims(q_batch_ids, axis=1), tf.expand_dims(k_batch_ids, axis=0))  # [Nq, Nk]
    # valid_indices = tf.where(batch_eq_mask)  # [P, 2] #gpu 会出现2025-06-24 11:42:36.381905: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Invalid argument: Expected shape dimensions to be non-negative, got -18436097

    # 第一种 分块
    # valid_indices = get_valid_indices(batch_eq_mask=batch_eq_mask) # [P, 2]

    # 第二种 mhta
    if is_mhta:
        k_range_indices = tf.range(tf.shape(k_indices)[0], dtype=tf.int32)  # [Nk]
        valid_indices = tf.stack([k_batch_ids, k_range_indices], axis=1)
    else:
        # batch_eq_mask = tf.equal(tf.expand_dims(q_batch_ids, axis=1), tf.expand_dims(k_batch_ids, axis=0))  # [Nq, Nk]
        # valid_indices = tf.where(
        #     batch_eq_mask)  # [P, 2] #gpu 会出现2025-06-24 11:42:36.381905: F tensorflow/core/framework/tensor_shape.cc:187] Non-OK-status: InitDims(dim_sizes) status: Invalid argument: Expected shape dimensions to be non-negative, got -18436097
        valid_indices = get_valid_indices_v2(q_batch_ids, k_batch_ids)
    # import pdb
    # pdb.set_trace()

    # 第三种
    # valid_indices = get_valid_indices_v2(q_batch_ids, k_batch_ids)
    valid_q_ids = tf.cast(valid_indices[:, 0], tf.int32)
    valid_k_ids = tf.cast(valid_indices[:, 1], tf.int32)

    # 多头拆分
    query_layer = tf.reshape(q_values, [-1, num_heads, size_per_head])  # [Nq, H, D_h]
    key_layer = tf.reshape(k_values, [-1, num_heads, size_per_head])  # [Nk, H, D_h]
    value_layer = tf.reshape(v_values, [-1, num_heads, v_size_per_head])  # [Nk, H, V_h]

    # import pdb
    # pdb.set_trace()
    selected_q = tf.gather(query_layer, valid_q_ids)  # [P, H, D_h]
    selected_k = tf.gather(key_layer, valid_k_ids)  # [P, H, D_h]

    # 点积
    # import pdb
    # pdb.set_trace()
    # scores = tf.reduce_sum(selected_q * selected_k, axis=-1)  # [P, H]
    scores = tf.einsum('...i,...i->...', selected_q, selected_k)
    d_k_sqrt = tf.cast(tf.math.sqrt(tf.cast(size_per_head, tf.float32)), scores.dtype)
    scores = scores / d_k_sqrt  # 除以根号下 d_k
    retuen_raw_scores = True
    if retuen_raw_scores:
        min_score = tf.reduce_min(scores)
        shifted_scores = scores - min_score + 0.001
        attention_scores = tf.reshape(shifted_scores, [-1])  # [P*H]

        # 构造注意力分数的索引

        q_batch_pos = tf.gather(q_indices, valid_q_ids)  # [P, 2]
        k_batch_pos = tf.gather(k_indices, valid_k_ids)  # [P, 2]

        # 为每个head扩展索引
        q_batch_pos_expand = tf.tile(tf.expand_dims(q_batch_pos, 1), [1, num_heads, 1])  # [P, H, 2]
        k_batch_pos_expand = tf.tile(tf.expand_dims(k_batch_pos, 1), [1, num_heads, 1])  # [P, H, 2]

        head_ids_expand = tf.tile(tf.expand_dims(tf.range(num_heads, dtype=tf.int32), 0),
                                  [tf.shape(valid_q_ids)[0], 1])  # [P, H]

        attention_indices = tf.stack([
            tf.cast(tf.reshape(q_batch_pos_expand[:, :, 0], [-1]), tf.int32),  # batch
            tf.cast(tf.reshape(head_ids_expand, [-1]), tf.int32),  # head
            tf.cast(tf.reshape(q_batch_pos_expand[:, :, 1], [-1]), tf.int32),  # q_pos
            tf.cast(tf.reshape(k_batch_pos_expand[:, :, 1], [-1]), tf.int32)  # k_pos
        ], axis=1)  # [P*H, 4]

        # 创建注意力分数的稀疏张量，形状为 [B, H, F, T]
        attention_scores_sparse = SparseTensor2dValue(
            indices=attention_indices,
            values=attention_scores,
            dense_shape=tf.convert_to_tensor([B, num_heads, F, T], dtype=tf.int64)
        )

    return {
        'raw_scores': scores,  # [P, H]
        'q_batch_ids': q_batch_ids,  # [Nq]
        'valid_q_ids': valid_q_ids,  # [P]
        'valid_k_ids': valid_k_ids,  # [P]
        # 'segment_ids': segment_ids,  # [P, H] 可选
    }


    if mask is not None:
        # 将 SparseTensor2dValue 转换为密集张量
        if isinstance(mask, SparseTensor2dValue):
            mask_dense = mask.to_dense()
        else:
            mask_dense = mask
        # 构造有效索引
        b_indices = tf.gather(q_batch_ids, valid_q_ids)
        q_pos_indices = tf.gather(q_indices[:, 1], valid_q_ids)
        k_pos_indices = tf.gather(k_indices[:, 1], valid_k_ids)

        # Convert all tensors to int32 type
        b_indices = tf.cast(b_indices, tf.int32)
        q_pos_indices = tf.cast(q_pos_indices, tf.int32)
        k_pos_indices = tf.cast(k_pos_indices, tf.int32)

        mask_indices = tf.stack([b_indices, q_pos_indices, k_pos_indices], axis=-1)

        # 提取有效 mask 值
        valid_mask = tf.gather_nd(mask_dense, mask_indices)  # [P]
        valid_mask = tf.cast(valid_mask, scores.dtype)

        # 扩展到每个头
        valid_mask = tf.tile(tf.expand_dims(valid_mask, -1), [1, num_heads])  # [P, H]

        # 应用 mask
        scores = scores + (1 - valid_mask) * -1e9

    # 分组ID
    head_ids = tf.range(num_heads, dtype=tf.int32)  # [H]
    valid_q_ids_expand = tf.expand_dims(valid_q_ids, 1)  # [P, 1]
    head_ids_expand = tf.expand_dims(head_ids, 0)  # [1, H]
    segment_ids = valid_q_ids_expand * num_heads + head_ids_expand  # [P, H]

    # Flatten
    flat_scores = tf.reshape(scores, [-1])  # [P*H]
    flat_segment_ids = tf.reshape(segment_ids, [-1])  # [P*H]

    # Softmax分组归一化
    num_segments = tf.reduce_max(flat_segment_ids) + 1
    max_per_segment = tf.math.unsorted_segment_max(flat_scores, flat_segment_ids, num_segments)
    stabilized_scores = flat_scores - tf.gather(max_per_segment, flat_segment_ids)
    exp_scores = tf.exp(stabilized_scores)
    sum_per_segment = tf.math.unsorted_segment_sum(exp_scores, flat_segment_ids, num_segments)
    scattered_sum = tf.gather(sum_per_segment, flat_segment_ids)
    softmax_scores_ = exp_scores / (scattered_sum + 1e-8)
    softmax_scores = tf.reshape(softmax_scores_, tf.shape(scores))  # [P, H]

    # 加权聚合V

    # 如果是mhta 不用gather
    if is_mhta:
        selected_v = value_layer  # [Nk, H, V_h]
    else:

        # selected_v = tf.gather(value_layer, valid_k_ids)  # [P, H, V_h]
        #
        unique_ids, idx = tf.unique(valid_k_ids)
        unique_v = tf.gather(value_layer, unique_ids)
        selected_v = tf.gather(unique_v, idx)
    #

    # weighted_v = selected_v * tf.expand_dims(softmax_scores, axis=-1)  # [P, H, V_h]
    # weighted_v_flat = tf.reshape(weighted_v, [-1, v_size_per_head])  # [P*H, V_h]
    # context = tf.math.unsorted_segment_sum(
    #     data=weighted_v_flat,
    #     segment_ids=flat_segment_ids,
    #     num_segments=num_segments
    # )  # [Nq*H, V_h]

    chunk_size = 8192  # 可根据显存情况调整
    total_p = selected_v.shape[0]
    context_accum = tf.zeros([num_segments, v_size_per_head], dtype=selected_v.dtype)
    for i in range(0, total_p, chunk_size):
        sv_chunk = selected_v[i:i + chunk_size]
        ss_chunk = softmax_scores[i:i + chunk_size]
        weighted_v_chunk = sv_chunk * tf.expand_dims(ss_chunk, axis=-1)
        weighted_v_flat_chunk = tf.reshape(weighted_v_chunk, [-1, v_size_per_head])
        flat_segment_ids_chunk = flat_segment_ids[i * num_heads:(i + chunk_size) * num_heads]
        context_chunk = tf.math.unsorted_segment_sum(
            data=weighted_v_flat_chunk,
            segment_ids=flat_segment_ids_chunk,
            num_segments=num_segments
        )
        context_accum += context_chunk
    context = context_accum

    # # 还原为[Nq, H, V_h]
    context = tf.reshape(context, [-1, num_heads, v_size_per_head])  # [Nq, H, V_h]
    # 合并head
    merged_context = tf.reshape(context, [-1, num_heads * v_size_per_head])  # [Nq, H*V_h]

    return {
        'scores': softmax_scores,  # [P, H]
        'raw_scores': scores,  # [P, H]
        'output': merged_context,  # [Nq, H*V_h]
        'q_batch_ids': q_batch_ids,  # [Nq]
        'valid_q_ids': valid_q_ids,  # [P]
        'valid_k_ids': valid_k_ids,  # [P]
        # 'segment_ids': segment_ids,  # [P, H] 可选
    }


# 示例调用
# 假设已经有 query_sparse, key_sparse, value_sparse, mask 等输入
# memory_usage = estimate_memory_usage(query_sparse, key_sparse, value_sparse, num_heads, size_per_head, v_size_per_head, mask)
# print(f"显存消耗估算: {memory_usage:.2f} GB")

if __name__ == '__main__':
    D = 8  # QK embedding dim
    V = 8  # V embedding dim
    H = 2  # num heads
    F = 2  # Q len
    T = 4  # KV len
    B = 2  # batch size

    # 固定随机种子，保证dense/sparse一致
    seed = 42
    tf.random.set_seed(seed)

    Q_dense, K_dense, V_dense = construct_test_qkv(D, V, H, F, T, B, output_sparse=False)
    tf.random.set_seed(seed)
    sparse_Q, sparse_K, sparse_V = construct_test_qkv(D, V, H, F, T, B, output_sparse=True)

    mask_dense = np.ones((B, F, T))
    mask_dense[:, 1, 2:] = 0  # 屏蔽部分位置
    sparse_mask = SparseTensor2dValue.from_dense(mask_dense)

    res = sparse_multihead_attention_fast_v2(
        query_sparse=sparse_Q,
        key_sparse=sparse_K,
        value_sparse=sparse_V,
        num_heads=4,
        size_per_head=8,
        v_size_per_head=16,
        mask=sparse_mask  # 传入 mask 矩阵
    )

    print(res)

    # print(res)
