"""
@Author: yanzx
@Date: 2021-08-03 10:06:40
@Desc:
"""


def find_point(arr, left, right):
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        elif arr[mid] < right:
            right = mid
        else:
            right -= 1
    return left


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 2, 3, 4]
    res = find_point(arr, 0, len(arr) - 1)
    print(res)
