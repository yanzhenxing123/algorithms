"""
@Author: yanzx
@Date: 2021-07-30 11:03:34
@Desc: 两个函数实现quick_sort

[1, 3, 2, 1, 5]

"""
import random


def partition(arr, left, right):
    # arr[left] 作为基准点
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot
    return right


def quick_sort(arr, left, right):
    # 左闭右闭
    if left < right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


if __name__ == '__main__':
    # 洗牌
    # random.shuffle(nums)
    nums = [1, 2, 3, 1, 1, 10, 2, 3, 4]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
