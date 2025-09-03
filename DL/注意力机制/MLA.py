"""
@Time: 2025/9/3 23:41
@Author: yanzx
@Description: 注意力计算 (self.mha) 是在压缩后的短序列 latent_tokens 上进行的，计算量大大减少 (O(L²) vs O(N²), L << N)。

1. 首先将输入展平，然后投影到一个大的空间，最后重塑为短序列
2. 计算att
3. 映射成长序列
"""

from torch import nn
from MHA import MultiHeadAttention

class MultiHeadLatentAttention(nn.Module):
    def __init__(self, d_model, num_heads, latent_seq_len):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        self.latent_seq_len = latent_seq_len

        # 投影矩阵，将长序列压缩为短序列（潜在序列）
        self.proj_down = nn.Linear(d_model, latent_seq_len * d_model)
        self.proj_up = nn.Linear(latent_seq_len * d_model, d_model)  # 可选的重建层

        # 标准 MHA 模块，但将在潜在序列上运行
        self.mha = MultiHeadAttention(d_model, num_heads)

    def forward(self, x):
        batch_size, seq_len, d_model = x.shape

        # 1. 压缩/降维: (batch_size, seq_len, d_model) -> (batch_size, latent_seq_len, d_model)
        # 首先将输入展平，然后投影到一个大的空间，最后重塑为短序列
        x_flattened = x.view(batch_size, -1)
        latent_tokens = self.proj_down(x_flattened)
        latent_tokens = latent_tokens.view(batch_size, self.latent_seq_len, d_model)

        # 2. 在潜在序列上计算标准注意力
        latent_output = self.mha(latent_tokens)  # (batch_size, latent_seq_len, d_model)

        # 3. (可选) 重建/上采样: (batch_size, latent_seq_len, d_model) -> (batch_size, seq_len, d_model)
        latent_flattened = latent_output.view(batch_size, -1)
        output = self.proj_up(latent_flattened)
        output = output.view(batch_size, seq_len, d_model)

        return output


# 示例：将10个token的序列压缩为4个潜在token
latent_seq_len = 4
mla = MultiHeadLatentAttention(d_model, num_heads, latent_seq_len)
output_mla = mla(x)
print("MLA Output Shape:", output_mla.shape)  # (2, 10, 64)