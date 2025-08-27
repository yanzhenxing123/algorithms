import torch


B = 24
seq_len = 100
emb_dim = 16

q = torch.randn(B, seq_len, emb_dim)
k = q.transpose(1, 2)

res = q @ k
print(res.shape) #  torch.Size([24, 100, 100])
print(res.shape) #  torch.Size([24, 100, 100])

