"""
@Time: 2025/9/3 23:17
@Author: yanzx
@Description: 可以理解为将 num_heads 分为 num_groups 组，每组有 num_heads // num_groups 个头
"""


class GroupedQueryAttention(nn.Module):
    def __init__(self, d_model, num_heads, num_groups):
        super().__init__()
        self.num_heads = num_heads
        self.num_groups = num_groups
        self.head_dim = d_model // num_heads

        assert num_heads % num_groups == 0, "num_heads must be divisible by num_groups"

        # Q 的投影是独立的（每个头一个）
        self.w_q = nn.Linear(d_model, d_model)
        # K 和 V 的投影是分组的
        # 输出维度：为 num_groups 个头投影，所以是 num_groups * head_dim
        self.w_k = nn.Linear(d_model, num_groups * self.head_dim)
        self.w_v = nn.Linear(d_model, num_groups * self.head_dim)

        self.w_o = nn.Linear(d_model, d_model)

    def forward(self, x):
        batch_size, seq_len, d_model = x.shape

        # 投影 Q (每个头独立)
        Q = self.w_q(x)
        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        # 投影 K, V (分组)
        K = self.w_k(x)  # (batch_size, seq_len, num_groups * head_dim)
        V = self.w_v(x)  # (batch_size, seq_len, num_groups * head_dim)

        # 将 K 和 V 重塑为 (batch_size, seq_len, num_groups, head_dim)
        K = K.view(batch_size, seq_len, self.num_groups, self.head_dim)
        V = V.view(batch_size, seq_len, self.num_groups, self.head_dim)

        # 现在需要将 K 和 V 的 num_groups 维度“扩展”到 num_heads
        # 例如，num_heads=8, num_groups=4 -> 每组有 8/4=2 个头共享同一套 K, V
        # 我们使用 repeat_interleave 在每个组后面重复“每个组对应的头数”次
        repeats = self.num_heads // self.num_groups
        K = K.unsqueeze(3)  # 增加一个维度用于重复
        K = K.repeat(1, 1, 1, repeats, 1)
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim)
        K = K.transpose(1, 2)  # -> (batch_size, num_heads, seq_len, head_dim)

        # 对 V 进行同样的操作
        V = V.unsqueeze(3).repeat(1, 1, 1, repeats, 1).view(batch_size, seq_len, self.num_heads,
                                                            self.head_dim).transpose(1, 2)

        # ... 现在 Q, K, V 的维度都是 (batch_size, num_heads, seq_len, head_dim)，可以进行注意力计算 ...

        attn_output = attn_output.transpose(1, 2).contiguous().view(batch_size, seq_len, d_model)
        output = self.w_o(attn_output)
        return output


# 示例：8个头，分成4组（每组2个头共享K,V）
num_groups = 4
gqa = GroupedQueryAttention(d_model, num_heads, num_groups)
output_gqa = gqa(x)
print("GQA Output Shape:", output_gqa.shape)  # (2, 10, 64)