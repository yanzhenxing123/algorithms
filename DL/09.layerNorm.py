"""
@Author: yanzx
@Time: 2025/8/25 15:32 
@Description:

LayerNorm(x) = γ[(x - μ) / 方差] + beta


RMSNorm(x) = γ 点乘 [x / √( (1/n) × Σ(xᵢ²) )]

1. RMSNorm 是什么？
RMSNorm（Root Mean Square Normalization，均方根归一化）是一种层归一化（Layer Normalization）技术的简化版本，
由 Google 在 2019 年提出。它主要用于深度学习模型中，用来稳定训练过程、加速收敛。

2. 为什么需要 RMSNorm？
在深度神经网络中，内部协变量偏移（Internal Covariate Shift）是一个常见问题：

∙每层的输入分布会随着训练过程不断变化
∙这会导致训练不稳定、收敛缓慢
∙需要更小的学习率和更仔细的参数初始化

RMSNorm 就是为了解决这个问题而设计的。
其提出的动机是 LayerNorm 运算量比较大，所提出的RMSNorm 性能和 LayerNorm 相当，但是可以节省7%到64%的运算

"""
import torch
from torch import nn


class LayerNorm(nn.Module):
    def __init__(self, hidden_size, eps=1e-6):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(hidden_size))
        self.beta = nn.Parameter(torch.zeros(hidden_size))

        self.eps = eps

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True)

        x_norm = (x - mean) / torch.sqrt(var + self.eps)

        output = self.gamma * x_norm + self.beta

        return output


class RMSNorm(nn.Module):
    def __init__(self, hidden_size, eps=1e-6):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(hidden_size))
        self.eps = eps




    def forward(self, x):
        """
        torch.Size([4, 3, 16])
        :param x:
        :return:
        """
        x_2 = torch.pow(x, 2)
        x_2_mean = torch.mean(x_2, dim=-1, keepdim=True) #
        x_norm = x / torch.sqrt(x_2_mean + self.eps)

        output = self.gamma * x_norm
        return output


if __name__ == '__main__':
    B = 4
    seq = 3
    emb_dim = 16
    x = torch.randn(B, seq, emb_dim)
    # print(x)

    rms_norm_layer = RMSNorm(emb_dim)
    res = rms_norm_layer(x)
    print(res)

