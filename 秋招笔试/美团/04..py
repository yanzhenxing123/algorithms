"""
@Time: 2025/8/16 20:11
@Author: yanzx
@Description: 
"""

import bisect


def count_triplets(n, arr):
    # 计算 left[i]，表示小于 a[i] 的元素个数
    left = [0] * n
    sorted_left = []

    for i in range(n):
        left[i] = bisect.bisect_left(sorted_left, arr[i])
        bisect.insort(sorted_left, arr[i])

    # 计算 right[i]，表示小于 a[i] 的元素个数
    right = [0] * n
    sorted_right = []

    for i in range(n - 1, -1, -1):
        right[i] = bisect.bisect_left(sorted_right, arr[i])
        bisect.insort(sorted_right, arr[i])

    # 计算满足条件的三元组的数量
    count = 0
    for j in range(1, n - 1):
        count += left[j] * right[j]

    return count


# 读取输入
n = int(input())  # 输入数组长度
arr = list(map(int, input().split()))  # 输入数组元素

# 输出结果
print(count_triplets(n, arr))
