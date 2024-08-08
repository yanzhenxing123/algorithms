"""
@Time: 2024/8/7 23:27
@Author: yanzx
@Desc: 
"""

from typing import List


def partition(nums: List[int], left: int, right: int):
    pivot = nums[left]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left


def quick_sort(nums: List[int], left: int, right: int):
    if left < right:
        pivot_index = partition(nums, left, right)
        quick_sort(nums, left, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, right)


if __name__ == '__main__':
    nums = [1, 3, 2, 0, 1, 1]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
