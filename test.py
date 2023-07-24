"""
this is a test py
"""

import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np

mnist_train = torchvision.datasets.FashionMNIST(root='./datasets/FashionMNIST', train=True, download=False,
                                                transform=transforms.ToTensor())
mnist_test = torchvision.datasets.FashionMNIST(root='./datasets/FashionMNIST', train=False, download=False,
                                               transform=transforms.ToTensor())
# 定义 batch_size
"""
batch_size是超参数,表示一轮训练多少个样本
shuffle是否打乱数据,True表示打乱数据
num_workers=0表示不开启多线程读取数据
"""

batch_size = 64  #

train_iter = torch.utils.data.DataLoader(mnist_train, batch_size=batch_size, shuffle=True,
                                         num_workers=0)  # num_workers=0,不开启多线程读取。
test_iter = torch.utils.data.DataLoader(mnist_test, batch_size=batch_size, shuffle=False, num_workers=0)

# 定义模型参数
num_inputs, num_outputs, num_hiddens = 784, 10, 256 # 输入 输出 隐藏
W1 = torch.tensor(np.random.normal(0, 0.01, (num_hiddens, num_inputs)), dtype=torch.float)
b1 = torch.zeros(num_hiddens, dtype=torch.float)
W2 = torch.tensor(np.random.normal(0, 0.01, (num_outputs, num_hiddens)), dtype=torch.float)
b2 = torch.zeros(num_outputs, dtype=torch.float)
params = [W1, b1, W2, b2]
for param in params:
    param.requires_grad_(requires_grad=True)



