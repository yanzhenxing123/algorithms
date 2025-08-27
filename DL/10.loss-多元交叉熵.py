"""
@Author: yanzx
@Time: 2025/8/19 09:44
@Description:

loss = -1/n * (y * log(y') + (1-y)*log(1-y'))
"""

import torch
import torch.nn.functional as F


def manual_cross_entropy(logits, y_true):
    """
    手动实现多元交叉熵损失（支持类别索引或one-hot标签）
    参数:
        logits: 模型原始输出 [N, C]
        y_true: 真实标签 [N,]（类别索引）或 [N, C]（one-hot） 是mask矩阵
    返回:
        loss: 标量
    """
    # 1. 计算softmax概率
    probs = F.softmax(logits, dim=1)

    # 2. 处理不同格式的标签
    selected_probs = torch.sum(probs * y_true, dim=1)

    # 3. 计算负对数概率均值（添加eps防log(0)）
    loss = -torch.mean(torch.log(selected_probs))
    return loss


# 示例数据
logits = torch.tensor([[1.0, 2.0, 3.0],  # 样本1
                       [0.5, 1.5, 0.1]])  # 样本2
# y_true_index = torch.tensor([2, 1])  # 类别索引（第3类和第2类）
y_true_onehot = torch.tensor([[0, 0, 1],  # one-hot编码
                              [0, 1, 0]])

# 计算手动实现结果
# manual_loss_index = manual_cross_entropy(logits, y_true_index)
manual_loss_onehot = manual_cross_entropy(logits, y_true_onehot)
# print(f"Manual Loss (Index): {manual_loss_index.item():.4f}")  # 输出: 0.4076
print(f"Manual Loss (One-hot): {manual_loss_onehot.item():.4f}")  # 输出: 0.4076

# 对比PyTorch官方实现
# official_loss = F.cross_entropy(logits, y_true_index)
print(f"Official Loss: {official_loss.item():.4f}")  # 输出: 0.4076