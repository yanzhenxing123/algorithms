"""
@Author: yanzx
@Date: 2021-10-04 14:25:43
@Desc:
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [nums[left], nums[right]]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = s.twoSum(nums, target)
    print(res)

