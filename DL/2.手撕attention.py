"""
@Author: yanzx
@Date: 2025/3/5 10:13
@Description:
"""

import torch
import math

x = torch.rand(4, 10)

l1 = torch.nn.Linear(10, 10)
l2 = torch.nn.Linear(10, 10)
l3 = torch.nn.Linear(10, 10)

q = l1(x)
k = l2(x)
v = l3(x)

torch.matmul(q, k.T)

print(q.shape)
print(k.shape)
print(v.shape)

res = torch.softmax((q @ k.T) / math.sqrt(10), dim=1) @ v

print(res)

# res = (q @ k.T) / math.sqrt(10) @ v
# print(res)
