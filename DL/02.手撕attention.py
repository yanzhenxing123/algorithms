"""
@Author: yanzx
@Date: 2025/3/5 10:13
@Description:
"""
import math

import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(42)  # CPU 随机种子


def simple_mha():
    x = torch.rand(4, 10)

    l1 = torch.nn.Linear(10, 10)
    l2 = torch.nn.Linear(10, 10)
    l3 = torch.nn.Linear(10, 10)

    q = l1(x)
    k = l2(x)
    v = l3(x)

    torch.matmul(q, k.T)

    print(q.shape)
    print(k.shape)
    print(v.shape)

    res = torch.softmax((q @ k.T) / math.sqrt(10), dim=1) @ v

    print(res)

    # res = (q @ k.T) / math.sqrt(10) @ v
    # print(res)


class EncoderBlock(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        """
        Args:
            d_model: 输入特征维度（例如 512）
            num_heads: 多头注意力的头数
            d_ff: 前馈网络隐藏层维度（通常为 d_model * 4）
            dropout: Dropout 概率
        """
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.feed_forward = FeedForward(d_model, d_ff, dropout)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        # 1. 多头自注意力 + 残差连接
        attn_output = self.self_attn(x, x, x, mask)
        x = x + self.dropout(attn_output)
        x = self.norm1(x)

        # 2. 前馈网络 + 残差连接
        ff_output = self.feed_forward(x)
        x = x + self.dropout(ff_output)
        x = self.norm2(x)

        return x


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads, dropout):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_k = d_model // num_heads
        self.num_heads = num_heads
        self.wq = nn.Linear(d_model, d_model)
        self.wk = nn.Linear(d_model, d_model)
        self.wv = nn.Linear(d_model, d_model)
        self.wo = nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)

        # 1. 线性投影并分头
        query = self.wq(query).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        key = self.wk(key).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        value = self.wv(value).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)

        # 2. 计算缩放点积注意力
        scores = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(torch.tensor(self.d_k, dtype=torch.float32))
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        attn = F.softmax(scores, dim=-1)
        attn = self.dropout(attn)
        output = torch.matmul(attn, value)

        # 3. 合并多头并输出
        output = output.transpose(1, 2).contiguous().view(batch_size, -1, self.num_heads * self.d_k)
        return self.wo(output)


class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)
        self.activation = nn.GELU()  # 或 nn.ReLU()

    def forward(self, x):
        return self.linear2(self.dropout(self.activation(self.linear1(x))))


if __name__ == '__main__':
    # 定义参数
    d_model = 512
    num_heads = 8
    d_ff = 2048
    batch_size = 32
    seq_len = 50

    # 创建 EncoderBlock 和随机输入
    encoder_block = EncoderBlock(d_model, num_heads, d_ff)
    x = torch.randn(batch_size, seq_len, d_model)  # 模拟输入序列

    # 前向传播
    output = encoder_block(x)
    print(output.shape)  # torch.Size([32, 50, 512])
