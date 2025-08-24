"""
@Time: 2025/8/24 17:23
@Author: yanzx
@Description:

softmax的导数：简单来说，Softmax的导数不是一个单一的值，而是一个雅可比矩阵（Jacobian Matrix）。这是因为Softmax函数将一个向量映射为另一个向量。

si = exp(xi) / (exp(xi)  + .... exp(xn) )



"""

import math


def softmax(nums):
    exp_nums = [math.exp(num) for num in nums]
    sum_exp_num = sum(exp_nums)
    return [x / sum_exp_num for x in exp_nums]


def softmax_derivative(softmax_output):
    length = len(softmax_output)
    jacobian_matrix = []
    for i in range(length):
        row = []
        for j in range(length):
            if i == j:
                item = softmax_output[i] * (1 - softmax_output[i])
            else:
                item = -softmax_output[i] * softmax_output[j]
            row.append(item)

        jacobian_matrix.append(row)

    return jacobian_matrix


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    softmax_out = softmax(nums)
    res = softmax_derivative(softmax_out)
    print(res)
