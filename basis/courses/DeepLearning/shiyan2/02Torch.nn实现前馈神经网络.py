"""
@Author: yanzx
@Date: 2023/7/24 15:45
@Description: ���ÿ⺯��ʵ��
"""

import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np

mnist_train = torchvision.datasets.FashionMNIST(root='../datasets/FashionMNIST', train=True, download=False,
                                                transform=transforms.ToTensor())
mnist_test = torchvision.datasets.FashionMNIST(root='../datasets/FashionMNIST', train=False, download=False,
                                               transform=transforms.ToTensor())
# ���� batch_size
"""
batch_size�ǳ�����,��ʾһ��ѵ�����ٸ�����
shuffle�Ƿ��������,True��ʾ��������
num_workers=0��ʾ���������̶߳�ȡ����
"""

batch_size = 64  #

train_iter = torch.utils.data.DataLoader(mnist_train, batch_size=batch_size, shuffle=True,
                                         num_workers=0)  # num_workers=0,���������̶߳�ȡ��
test_iter = torch.utils.data.DataLoader(mnist_test, batch_size=batch_size, shuffle=False, num_workers=0)

# ����ģ�Ͳ���
num_inputs, num_outputs, num_hiddens = 784, 10, 256  # ���� ��� ����
W1 = torch.tensor(np.random.normal(0, 0.01, (num_hiddens, num_inputs)), dtype=torch.float)
b1 = torch.zeros(num_hiddens, dtype=torch.float)
W2 = torch.tensor(np.random.normal(0, 0.01, (num_outputs, num_hiddens)), dtype=torch.float)
b2 = torch.zeros(num_outputs, dtype=torch.float)
params = [W1, b1, W2, b2]
for param in params:
    param.requires_grad_(requires_grad=True)


def relu(X):
    """
    relu�����
    :param X:
    :return:
    """
    return torch.max(input=X, other=torch.tensor(0.0))


# ��������ʧ����
loss = torch.nn.CrossEntropyLoss()


# ����ݶ��½�����
def SGD(params, lr):
    for param in params:
        param.data -= lr * param.grad


# ����ģ��
def net(X):
    """
    ģ��
    :param X:
    :return:
    """
    X = X.view((-1, num_inputs))  # (1,  784)
    H = relu(torch.matmul(X, W1.t()) + b1)  # ���ز�
    return torch.matmul(H, W2.t()) + b2  # �����


# ����׼ȷ��
def evaluate_accuracy(data_iter, net):
    """
    ׼ȷ��
    :param data_iter:
    :param net:
    :return:
    """
    acc_sum, n = 0.0, 0
    for X, y in data_iter:
        acc_sum += (net(X).argmax(dim=1) == y).float().sum().item()
        n += y.shape[0]
    return acc_sum / n


# ģ��ѵ������
def train(net, train_iter, test_iter, loss, num_epochs, batch_size, params=None, lr=None, optimizer=None):
    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
        for X, y in train_iter:
            y_hat = net(X)
            l = loss(y_hat, y).sum()
            # �ݶ�����
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
        test_acc = evaluate_accuracy(test_iter, net)
        print(' epoch %d,loss %.4f,train acc %.3f,test acc %.3f' % (
            epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc))


num_epochs = 5
lr = 0.1


class FlatterLayer(torch.nn.Module):
    """
    ��ƽ
    """
    def __init__(self):
        super(FlatterLayer, self).__init__()

    def forward(self, x: torch.Tensor):
        return x.view(x.shape[0], -1)


class 