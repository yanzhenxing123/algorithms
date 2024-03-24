"""
@Time: 2024/3/23 09:29
@Author: yanzx
@Desc:
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]

"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        时间复杂度为o(n)
        记录数组中有多少个0即可
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for k in range(j, len(nums)):
            nums[k] = 0

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        时间复杂度为o(n2)
        挪动数组
        """
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == 0:
                for i in range(left, right):
                    nums[i] = nums[i + 1]
                nums[right] = 0
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    res = s.moveZeroes(nums)
    print(nums)
