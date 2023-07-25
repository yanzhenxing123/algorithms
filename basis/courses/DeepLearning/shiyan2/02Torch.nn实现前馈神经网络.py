"""
@Author: yanzx
@Date: 2023/7/24 15:45
@Description: 调用库函数实现
"""

import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
from torch import nn
from torch.nn import init
from torch.optim import SGD
import matplotlib.pyplot as plt

mnist_train = torchvision.datasets.FashionMNIST(root='../datasets/FashionMNIST', train=True, download=False,
                                                transform=transforms.ToTensor())
mnist_test = torchvision.datasets.FashionMNIST(root='../datasets/FashionMNIST', train=False, download=False,
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
num_inputs, num_outputs, num_hiddens = 784, 10, 256  # 输入 输出 隐藏
W1 = torch.tensor(np.random.normal(0, 0.01, (num_hiddens, num_inputs)), dtype=torch.float)
b1 = torch.zeros(num_hiddens, dtype=torch.float)
W2 = torch.tensor(np.random.normal(0, 0.01, (num_outputs, num_hiddens)), dtype=torch.float)
b2 = torch.zeros(num_outputs, dtype=torch.float)
params = [W1, b1, W2, b2]
for param in params:
    param.requires_grad_(requires_grad=True)


class FlatterLayer(torch.nn.Module):
    """
    铺平
    """

    def __init__(self):
        super(FlatterLayer, self).__init__()

    def forward(self, x: torch.Tensor):
        return x.view(x.shape[0], -1)


num_inputs, num_outputs, num_hiddens = 784, 10, 256
net = nn.Sequential(
    FlatterLayer(),
    nn.Linear(num_inputs, num_hiddens),
    nn.ReLU(),
    nn.Linear(num_hiddens, num_outputs),
)

for params in net.parameters():
    nn.init.normal_(params, mean=0, std=0.01)


# 计算准确率
def evaluate_accuracy(data_iter, net, loss):
    """
    准确率
    :param data_iter:
    :param net:
    :return:
    """
    acc_sum, n = 0.0, 0
    for X, y in data_iter:
        acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
        l = loss(net(X), y).sum()
        test_l_sum = l.item()
        n += y.shape[0]
    return acc_sum / n, test_l_sum / n


num_epochs = 5
lr = 0.1

loss = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr)


# 模型训练函数
def train(net, train_iter, test_iter, loss, num_epochs, batch_size, params=None, lr=None, optimizer=None):
    test_loss = []
    train_loss = []
    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
        for X, y in train_iter:
            y_hat = net(X)
            l = loss(y_hat, y).sum()
            # 梯度清零
            if optimizer is not None:
                optimizer.zero_grad()
            elif params is not None and params[0].grad is not None:
                for param in params:
                    param.grad.data.zero_()
            l.backward()
            if optimizer is None:
                SGD(params, lr)
            else:
                optimizer.step()
            train_l_sum += l.item()
            train_acc_sum += (y_hat.argmax(dim=1) == y).sum().item()
            n += y.shape[0]
        test_acc, test_l = evaluate_accuracy(test_iter, net, loss)
        train_loss.append(train_l_sum / n)
        test_loss.append(test_l)
        print('epoch %d, loss%.4f,train acc %.3f,test acc %.3f' % (
        epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc))
    return train_loss, test_loss


train_loss, test_loss = train(net, train_iter, test_iter, loss, num_epochs, batch_size, net.parameters(), lr, optimizer)

x = np.linspace(0, len(train_loss), len(train_loss))
plt.plot(x, train_loss, label="train_loss", linewidth=1.5)
plt.plot(x, test_loss, label="test_loss", linewidth=1.5)
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend()
plt.show()
