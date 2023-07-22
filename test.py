"""
this is a test py
"""


import torch as t
from torch.autograd import Variable as v


# simple gradient
a = v(t.FloatTensor([2, 3]), requires_grad=True)
b = a + 3
c = b * b * 3
out = c.mean()
out.backward()
print('*'*10)
print('=====simple gradient======')
print('input')
print(a.data)
# print('compute result is')
# print(out.data[0])
print('input gradients are')

print(a.grad.data)


