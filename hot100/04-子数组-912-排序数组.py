"""
@Time: 2025/3/24 17:05
@Author: yanzx
@Desc: 
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, left, right):
        if left < right:
            pivot_index = self.partition(nums, left, right)
            self.quick_sort(nums, left, pivot_index - 1)
            self.quick_sort(nums, pivot_index + 1, right)

    def partition(self, nums, left, right):
        pivot = nums[left] # zhe'l
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [5, 1, 1, 2, 0, 0]
    res = s.sortArray(nums)
    print(res)
