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


if __name__ == '__main__':
    arr = [_ for _ in range(100)]
    print(arr)
    index = binary_search(arr, 0, len(arr) - 1, 20)
    print(index)
