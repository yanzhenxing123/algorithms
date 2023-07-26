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
    """
    找左边界
    :param arr:
    :param left:
    :param right:
    :param target:
    :return:
    """
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
