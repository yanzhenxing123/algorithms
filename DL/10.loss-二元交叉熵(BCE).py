"""
@Author: yanzx
@Time: 2025/8/19 09:44 
@Description:

loss = -1/n * (y * log(p) + (1-y)*log(1-p))
"""

import torch


def manual_bce_with_logits(logits, y_true):
    """
    手动实现 BCEWithLogits（含 Sigmoid + BCE）
    -y * torch.log(probs) + (1 - y_true) * torch.log(1 - probs + eps)
    参数:
        logits: 模型原始输出 (未经过 Sigmoid), shape: (N, *)
        y_true: 真实标签 (0.0 或 1.0), shape: 与 logits 相同
    返回:
        loss: 标量
    """
    # 1. 对 logits 应用 Sigmoid 得到概率
    probs = torch.sigmoid(logits)

    # 2. 添加极小值 eps 避免 log(0) 数值错误
    eps = 1e-8

    # 3. 计算 BCE
    loss = -torch.mean(
        y_true * torch.log(probs) + (1 - y_true) * torch.log(1 - probs)
    )

    return loss


# 示例数据
logits = torch.tensor([[1.2], [-0.5], [0.3]])  # 模型原始输出
y_true = torch.tensor([[1.0], [0.0], [1.0]])  # 真实标签

# 计算手动实现结果
manual_loss = manual_bce_with_logits(logits, y_true)
print("Manual BCE:", manual_loss.item())  # 输出: 0.5027

# 对比 PyTorch 官方实现
official_loss = torch.nn.BCEWithLogitsLoss()(logits, y_true)
print("Official BCEWithLogitsLoss:", official_loss.item())  # 输出: 0.5027