import torch
from torch.nn import functional as F


def InfoNCE(view1, view2, temperature: float, b_cos: bool = True):
    if b_cos:
        view1, view2 = F.normalize(view1, dim=1), F.normalize(view2, dim=1)

    pos_score = (view1 @ view2.T) / temperature
    score = torch.diag(F.log_softmax(pos_score, dim=1))
    return -score.mean()


def InfoNCE_simple(view1, view2, temperature=0.07):
    """简化版本，更容易理解"""
    # 归一化
    view1 = F.normalize(view1, dim=1)  # torch.Size([4, 8])
    view2 = F.normalize(view2, dim=1)  # torch.Size([4, 8])

    # 计算相似度矩阵
    sim_matrix = view1 @ view2.T / temperature  # torch.Size([4, 4])

    # 正样本：对角线（自己与自己）
    pos_sim = torch.diag(sim_matrix)  # torch.Size([4])

    # 负样本：非对角线
    mask = torch.eye(sim_matrix.shape[0], dtype=torch.bool)  # torch.Size([4, 4]) 用于创建对角矩阵，对角是1，其他是0
    neg_sim = sim_matrix[~mask].view(sim_matrix.shape[0], -1)

    # 构建logits: [正样本, 负样本...]
    logits = torch.cat([pos_sim.unsqueeze(1), neg_sim], dim=1)

    # 标签都是0（正样本在第一个位置）
    labels = torch.zeros(len(pos_sim), dtype=torch.long, device=view1.device)

    return F.cross_entropy(logits, labels)


def cal_cl_loss(temp, idx, user_view1, user_view2, item_view1, item_view2):
    temp = 0.5
    u_idx = torch.unique(idx[0].type(torch.long))
    i_idx = torch.unique(idx[1].type(torch.long))
    user_cl_loss = InfoNCE(user_view1[u_idx], user_view2[u_idx], temp)
    item_cl_loss = InfoNCE(item_view1[i_idx], item_view2[i_idx], temp)
    return user_cl_loss + item_cl_loss


def approx_infoNCE_loss(q, k, temp):
    # 计算query和key的相似度得分
    similarity_scores = torch.matmul(q, k.t())  # 矩阵乘法计算相似度得分

    # 计算相似度得分的温度参数

    # 计算logits
    logits = similarity_scores / temp

    # 构建labels（假设有N个样本）
    N = q.size(0)
    labels = torch.arange(N).to(logits.device)

    # 计算交叉熵损失
    loss = F.cross_entropy(logits, labels)

    return loss


if __name__ == '__main__':
    print("=" * 50)
    print("测试用例1：基本功能测试")
    print("=" * 50)

    # 创建简单的测试数据
    batch_size = 4
    feature_dim = 8

    # 视角1：随机特征
    view1 = torch.randn(batch_size, feature_dim)
    # 视角2：视角1 + 小噪声（模拟数据增强）
    view2 = view1 + 0.1 * torch.randn_like(view1)

    print(f"视角1形状: {view1.shape}")
    print(f"视角2形状: {view2.shape}")
    print(f"视角1前3个特征: {view1[0, :3]}")
    print(f"视角2前3个特征: {view2[0, :3]}")

    # 测试不同温度参数
    temperatures = [0.01, 0.07, 0.5, 1.0]

    for temp in temperatures:
        loss1 = InfoNCE(view1, view2, temp)
        loss2 = InfoNCE_simple(view1, view2, temp)
        loss3 = approx_infoNCE_loss(view1, view2, temp)
        print(f"温度={temp:.2f}: 原始版本={loss1.item():.4f}, 简化版本={loss2.item():.4f}, approx_infoNCE_loss={loss3.item():.4f}")

    print(view1)
    print(view2)
