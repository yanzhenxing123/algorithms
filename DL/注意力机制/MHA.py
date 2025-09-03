"""
@Time: 2025/9/3 23:16
@Author: yanzx
@Description: 
"""

from torch import nn


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads

        # 每个头都有独立的投影矩阵
        self.w_q = nn.Linear(d_model, d_model)  # 输出维度为 num_heads * head_dim = d_model
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)

        self.w_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        batch_size, seq_len, d_model = x.shape

        # 独立投影得到 Q, K, V
        Q = self.w_q(x)  # (batch_size, seq_len, d_model)
        K = self.w_k(x)  # (batch_size, seq_len, d_model)
        V = self.w_v(x)  # (batch_size, seq_len, d_model)

        # 重塑为 (batch_size, num_heads, seq_len, head_dim)
        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        # ... 这里进行 Q@K.T / sqrt(d_k) -> Softmax -> @ V 的计算 ...
        # attn_output: (batch_size, num_heads, seq_len, head_dim)

        # 将多头输出拼接回来
        attn_output = attn_output.transpose(1, 2).contiguous().view(batch_size, seq_len, d_model)

        # 最终输出投影
        output = self.w_o(attn_output)
        return output


mha = MultiHeadAttention(d_model, num_heads)
output_mha = mha(x)
print("MHA Output Shape:", output_mha.shape)  # (2, 10, 64)