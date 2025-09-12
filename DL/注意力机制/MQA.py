"""
@Time: 2025/9/3 23:17
@Author: yanzx
@Description: kv是单个头，所以在映射时需要把kv的最后一维映射为 head_dim
"""


class MultiQueryAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads

        # Q 的投影是独立的（每个头一个）
        self.w_q = nn.Linear(d_model, d_model)
        # K 和 V 的投影是共享的（只有一个头）
        # 注意输出维度：只为单个头投影，所以是 head_dim，而不是 d_model
        self.w_k = nn.Linear(d_model, self.head_dim)
        self.w_v = nn.Linear(d_model, self.head_dim)

        self.w_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        batch_size, seq_len, d_model = x.shape

        # 投影 Q (每个头独立)
        Q = self.w_q(x)  # (batch_size, seq_len, d_model)
        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        # 投影 K, V (共享)
        K = self.w_k(x)  # (batch_size, seq_len, head_dim)
        V = self.w_v(x)  # (batch_size, seq_len, head_dim)

        # 为了计算注意力，需要将 K 和 V 的维度扩展为 (batch_size, 1, seq_len, head_dim)
        # 这样可以利用广播机制，与 (batch_size, num_heads, seq_len, head_dim) 的 Q 进行计算
        K = K.unsqueeze(1)  # 在“头”的维度上增加一维
        V = V.unsqueeze(1)

        # ... 这里进行注意力计算 ...
        # Q (batch_size, num_heads, seq_len, head_dim)
        # K (batch_size, 1, seq_len, head_dim) -> 广播为 (batch_size, num_heads, seq_len, head_dim)
        # 同理 V
        # attn_output: (batch_size, num_heads, seq_len, head_dim)

        # 将多头输出拼接回来
        attn_output = attn_output.transpose(1, 2).contiguous().view(batch_size, seq_len, d_model)
        output = self.w_o(attn_output)
        return output


mqa = MultiQueryAttention(d_model, num_heads)
output_mqa = mqa(x)
print("MQA Output Shape:", output_mqa.shape)  # (2, 10, 64)