"""
@Author: yanzx
@Date: 2023/5/20 18:57
@Description: 
"""

import math
import numpy as np
import matplotlib.pyplot as plt



def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def softplus(x):
    return np.log(1 + np.exp(x))

def swish(x, beta):
    return x * sigmoid(beta * x)


def get_central_ax():
    ax = plt.gca()  # get current axis 获得坐标轴对象

    # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # 指定下边的边作为 x 轴 指定左边的边为 y 轴
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.spines['bottom'].set_position(('data', 0))  # 指定 data 设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    ax.spines['left'].set_position(('data', 0))

    return ax

if __name__ == '__main__':
    x = np.arange(-8.0, 8.0, 0.0001)
    x_ticks = np.arange(-8.0, 8.1, 2)
    y_ticks = np.arange(0.1, 1.1, 0.3)

    y1 = sigmoid(x)
    y2 = tanh(x)
    y3 = relu(x)
    y4 = softplus(x)

    ax = get_central_ax()
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    # ax = plt.subplot(111)
    ax.plot(x, y1, color='black')
    # ax.plot(x, y2, linestyle='--')
    # ax.plot(x, y3, linestyle='--')
    # ax.plot(x, y4, linestyle='--')
    # ax.legend(['sigmoid', 'tanh', 'ReLU', 'softplus'])
    plt.show()
