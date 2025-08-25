"""
@Author: yanzx
@Time: 2025/8/25 15:32 
@Description:

layerNorm(x) = γ[(x - μ) / 方差] + beta

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



if __name__ == '__main__':
    B = 4
    seq = 3
    emb_dim = 16
    x = torch.randn(B, seq, emb_dim)
    print(x)
