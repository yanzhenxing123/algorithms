"""
@Author: yanzx
@Date: 2022/3/18 0:14
@Description: 
"""
from typing import List


def binary_search(arr: List, target: int):
    # 左闭右闭
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid

    return None


if __name__ == '__main__':
    # 测试二分
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(arr)
    res = binary_search(arr, 10)
    print(res)