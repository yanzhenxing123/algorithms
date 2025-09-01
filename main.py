import torch
import torch.nn as nn


x = torch.randn(5, 16)

wq = nn.Linear(16, 16)

q = wq(x)
k = wq(x)
v = wq(x)


print(q @ k.T)

