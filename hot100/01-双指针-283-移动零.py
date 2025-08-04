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

思路：时间复杂度最好为O(n)
遍历记录0的数量，并且把非零元素移动到前边

"""

from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        时间复杂度为o(n)
        挪动数组
        """
        if not nums:
            return
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0

    def moveZeroes_2(self, nums: List[int]) -> None:
        if not nums:
            return
        index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[index] = nums[i]
            index += 1
        for i in range(index, len(nums)):
            nums[i] = 0


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    res = s.moveZeroes(nums)
    print(nums)
