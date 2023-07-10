"""
@Author: yanzx
@Date: 2023/7/9 15:54
@Description: 一、Pytorch基本操作考察（平台课+专业课）
"""

import torch

"""
1. 使用 tensor 初始化一个 1 × 3 的矩阵M 和一个2 × 1 的矩阵N，对两矩阵进行减法操作（要求实现三种不同的形式），
给出结果并分析三种方式的不同（如果出现报错，分析报错的原因），同时需要指出在计算过程中发生了什么
"""

M = torch.rand(1, 3)
N = torch.rand(2, 1)

print(M)
print(N)

print(M-N)

M.sub_(N)
print(M)






