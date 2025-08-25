"""
@Author: yanzx
@Time: 2025/8/25 15:40 
@Description: 
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class MarginLoss(nn.Module):
    """
    基础的 Margin Loss 实现

    公式: L = max(0, margin + positive_distance - negative_distance)
    """

    def __init__(self, margin=1.0, distance_type='euclidean'):
        """
        Args:
            margin: 边界值，正负样本距离的最小差值
            distance_type: 距离类型 ('euclidean', 'cosine', 'manhattan')
        """
        super().__init__()
        self.margin = margin
        self.distance_type = distance_type

    def forward(self, anchor, positive, negative):
        """
        计算 Margin Loss

        Args:
            anchor: 锚点样本 [batch_size, feature_dim]
            positive: 正样本 [batch_size, feature_dim]
            negative: 负样本 [batch_size, feature_dim]

        Returns:
            loss: 平均损失值

        目标：正样本 - 负样本 > margin
        """
        # 计算距离
        pos_dist = self._compute_distance(anchor, positive)
        neg_dist = self._compute_distance(anchor, negative)

        # Margin Loss 公式
        loss = torch.clamp(self.margin + neg_dist  - pos_dist, min=0.0)

        return loss.mean()

    def _compute_distance(self, x1, x2):
        """计算两个张量之间的距离"""
        if self.distance_type == 'euclidean':
            return torch.norm(x1 - x2, dim=1)
        elif self.distance_type == 'cosine':
            # 余弦距离 = 1 - 余弦相似度
            cos_sim = F.cosine_similarity(x1, x2, dim=1)
            return 1 - cos_sim
        elif self.distance_type == 'manhattan':
            return torch.sum(torch.abs(x1 - x2), dim=1)
        else:
            raise ValueError(f"不支持的距离类型: {self.distance_type}")


# 测试基础实现
def test_basic_margin_loss():
    """测试基础 Margin Loss"""

    # 创建测试数据
    batch_size = 4
    feature_dim = 128

    anchor = torch.randn(batch_size, feature_dim)
    positive = torch.randn(batch_size, feature_dim)
    negative = torch.randn(batch_size, feature_dim)

    # 创建损失函数
    margin_loss = MarginLoss(margin=1.0, distance_type='euclidean')

    # 计算损失
    loss = margin_loss(anchor, positive, negative)

    print(f"基础 Margin Loss: {loss.item():.4f}")

    return loss


res = test_basic_margin_loss()
print(res)
