'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-10-05 16:03:32
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-10-05 17:36:37
FilePath: /algorithms/utils/二分查找.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
@Author: yanzx
@Date: 2021-08-03 10:01:30
@Desc: 
"""


def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_right(arr, left, right, target):
    """
    找右边界
    :param arr:
    :param left:
    :param right:
    :param target:
    :return:
    """
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    # 返回的left-1就是右边界
    return left


def binary_search_left(arr, left, right, target):

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    # 返回的right+1就是左边界
    return right


if __name__ == '__main__':
    arr = [
        1, 2, 3, 3, 3, 3, 3, 3, 5, 5, 6, 7
    ]
    index = binary_search_right(arr, 0, len(arr) - 1, 3)  # index = 8
    print(index)
    index = binary_search_left(arr, 0, len(arr) - 1, 3)  # index = 1
    print(index)
    index = binary_search_right(arr, 0, len(arr) - 1, 4)  # index = 8
    print(index)
    index = binary_search_left(arr, 0, len(arr) - 1, 4)  # index = 7
    

    print(index)
