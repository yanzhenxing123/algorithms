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

import torch
import torch.nn as nn

# 假设输入特征数量为n，输出特征数量为m
n = 784  # 输入特征数，假设输入图像大小为28x28，展平后为784维
m = 64  # 输出特征数，可以自行设定

# 定义全连接层
fc_layer = nn.Linear(n, m)

# 假设我们有一个输入张量x，大小为(n,)，表示一个展平的输入图像
x = torch.randn(n)

# 前向传播，将x输入全连接层进行线性变换
output = fc_layer(x)

# 输出的大小为(m,)，表示全连接层的输出特征
print(output.size())

