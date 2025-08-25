import numpy as np


class Relu:
    def forward(self, x):
        self.x = x
        return np.maximum(0, x)

    def backward(self, grad_output, lr):  # 这里的lr没有用到，但是为了保持参数接口的一致性，还是保留了
        return grad_output * (self.x > 0)  # relu函数的一阶导数，大于0部分为1，小于0部分为0


class LinearLayer:
    def __init__(self, input_c, output_c):
        # y = x @ w + b
        # self.w = np.random.rand(input_c, output_c)
        self.w = np.random.rand(input_c, output_c) * 0.001  # 这里乘上0.001是为了防止结果太大，梯度爆炸
        self.b = np.zeros(output_c)

    def forward(self, x):
        self.x = x  # 这里保存输入，为了后续在反向传播中计算梯度
        # y = x @ w + b
        return np.dot(x, self.w) + self.b

    def backward(self, grad_output, lr):
        # linear层的梯度计算，涉及三个参数，x，w，b，为 dx, dw, db
        # 其中，dw和db是为了更新w和b
        # dx是为了计算下一层的梯度，链式法则

        # y = x @ w + b
        # dl / dx = dl / dy * dy / dx = grad_output * w
        # 这里要注意矩阵的维度要对齐
        grad_input = np.dot(grad_output, self.w.T)

        # dl / dw = dl / dy * dy / dw = grad_output * x
        # 这里要注意矩阵的维度要对齐
        w_grad = np.dot(self.x.T, grad_output)

        b_grad = np.sum(grad_output, axis=0)

        # 更新w和b的参数
        self.w -= lr * w_grad
        self.b -= lr * b_grad

        return grad_input


class MLP:
    def __init__(self, input_c, hidden_c, output_c, layers_num):
        self.layers = []

        # 初始化网络第一层
        self.layers.append(LinearLayer(input_c, hidden_c))
        self.layers.append(Relu())

        # 初始化网络中间层
        for i in range(layers_num - 2):
            self.layers.append(LinearLayer(hidden_c, hidden_c))
            self.layers.append(Relu())

        # 初始化网络最后一层，注意，最后一层没有relu激活函数
        self.layers.append(LinearLayer(hidden_c, output_c))

    def forward(self, x):
        res = x
        for layer in self.layers:
            res = layer.forward(res)
        return res

    def backward(self, grad_output, lr):
        grad = grad_output

        # 倒序遍历每一层，反向传播，计算每一层梯度
        # for layer in reversed(self.layers):
        for layer in self.layers[::-1]:
            grad = layer.backward(grad, lr)

        return grad


if __name__ == '__main__':
    input_data = np.random.rand(2, 8)
    input_c = 8
    hidden_c = 16
    output_c = 3
    layers = 5
    target = np.random.rand(2, 3)

    mlp_model = MLP(input_c, hidden_c, output_c, layers)

    # print(mlp_model.layers)

    for i in range(10):
        print(f'[Epoch: {i} / 100]', end='   ')
        res = mlp_model.forward(input_data)

        # 计算损失loss，这里使用mse，均方误差函数
        loss = ((res - target) ** 2).mean()

        # 损失对于最后一层输出res的梯度
        loss_grad = 2 * (res - target)

        # 反向传播，计算每一层梯度
        mlp_model.backward(loss_grad, lr=0.1)

        print(f'[loss: {loss}]')
