import torch

x = torch.randn(4, 100)

layer_norm = torch.nn.BatchNorm1d(num_features=100)

x = layer_norm(x)

print(torch.mean(x, dim=0))
print(torch.var(x, dim=0))