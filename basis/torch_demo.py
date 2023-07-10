"""
@Author: yanzx
@Date: 2023/7/5 11:34
@Description: some torch demos
"""

import torch
from torch.autograd import Variable

x = torch.rand(1000)  # (0, 1)之间的均匀分布
print(x)
y = torch.randn(1)  # 均值为0，方差为1的正态分布
print(y.item())