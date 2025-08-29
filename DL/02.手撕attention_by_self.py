import torch
import torch.nn as nn
from torch.nn import functional as F

torch.manual_seed(42)


class MultiHeadSelfAttention(nn.Module):
    def __init__(self, dim_in, num_heads=8):
        super(MultiHeadSelfAttention, self).__init__()
        assert dim_in % num_heads == 0, "dim_in must be divisible by num_heads"
        self.dim_in = dim_in
        self.num_heads = num_heads
        self.w_q = nn.Linear(dim_in, dim_in)
        self.w_k = nn.Linear(dim_in, dim_in)
        self.w_v = nn.Linear(dim_in, dim_in)
        self.dropout = nn.Dropout()
        self.linear = nn.Linear(dim_in, dim_in)

    def forward(self, x, padding_mask=None, causal_mask=None):
        bs, seq_len, emb_dim = x.shape
        assert emb_dim == self.dim_in
        size_per_head = emb_dim // self.num_heads

        # 生成 Q, K, V 并分头
        q = self.w_q(x).reshape(bs, seq_len, self.num_heads, size_per_head).transpose(1, 2)  # (B, H, F, D/H)
        k = self.w_k(x).reshape(bs, seq_len, self.num_heads, size_per_head).transpose(1, 2)  # (B, H, F, D/H)
        v = self.w_v(x).reshape(bs, seq_len, self.num_heads, size_per_head).transpose(1, 2)  # (B, H, F, D/H)

        # 计算注意力分数
        attn_scores = (q @ k.transpose(2, 3)) / (size_per_head ** 0.5)  # (B, H, F, F)
        torch.matmul
        # 处理 padding_mask（修正点）
        if padding_mask is not None:
            # 将 padding_mask 从 (B, F) 扩展为 (B, 1, 1, F)
            padding_mask = padding_mask.unsqueeze(1).unsqueeze(2)  # (B, 1, 1, F)
            # 将 padding=0 的位置填充为负无穷
            attn_scores = attn_scores.masked_fill(padding_mask == 0, -1e9)

        # 处理 causal_mask（可选）
        if causal_mask is not None:
            # causal_mask 的形状应为 (1, F, F) 或 (F, F)
            causal_mask = causal_mask.unsqueeze(0)  # (1, F, F)
            attn_scores = attn_scores.masked_fill(causal_mask == 0, -1e9)

        # 计算注意力权重和输出
        attn_weights = F.softmax(attn_scores, dim=-1)
        output = (attn_weights @ v).transpose(1, 2).reshape(bs, seq_len, emb_dim)
        return self.linear(output)


if __name__ == '__main__':
    # 初始化模型和输入
    mhsa = MultiHeadSelfAttention(dim_in=32, num_heads=8)
    x = torch.rand(4, 10, 32)  # (B, F, D)

    # 生成 padding_mask（修正点）
    padding_mask = torch.tensor([
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # 第1个样本：前5有效，后5 padding
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # 第2个样本：前3有效
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],  # 第3个样本：前8有效
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 第4个样本：仅第1有效
    ]).bool()  # (B, F)

    # 生成 causal_mask（可选）
    causal_mask = torch.tril(torch.ones(10, 10)).bool()  # (F, F)
    # 测试输出
    output_with_padding_mask = mhsa(x, padding_mask=padding_mask)
    output_with_causal_mask = mhsa(x, causal_mask=causal_mask)
    print("Output shape with padding mask:", output_with_padding_mask.shape)
    print("Output shape with causal mask:", output_with_causal_mask.shape)
