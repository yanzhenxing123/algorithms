"""
@Author: yanzx
@Time: 2025/8/27 14:37 
@Description: 
"""

import torch
import torch.nn.functional as F


def approx_infoNCE_loss(q, k):
    # 计算query和key的相似度得分
    similarity_scores = torch.matmul(q, k.t())  # 矩阵乘法计算相似度得分

    # 计算相似度得分的温度参数
    temperature = 0.07

    # 计算logits
    logits = similarity_scores / temperature

    # 构建labels（假设有N个样本）
    N = q.size(0)
    labels = torch.arange(N).to(logits.device)

    # 计算交叉熵损失
    loss = F.cross_entropy(logits, labels)

    return loss

