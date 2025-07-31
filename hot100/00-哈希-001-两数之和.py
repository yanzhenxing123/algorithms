"""
@Author: yanzx
@Date: 2025/2/13 14:28
@Description:
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        判断另一个元素是否在字典中，如果在就return 不在就将此元素存储在其中
        """
        num2index = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in num2index:
                return [index, num2index[another_num]]
            num2index[num] = index

    def twoSum_2nd(self, nums: List[int], target: int) -> List[int]:
        num2index = {}

        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in num2index:
                return [index, num2index[another_num]]
            num2index[num] = index

    def twoSum_3nd(self, nums: List[int], target: int) -> List[int]:
        """
        遍历一遍，存储在num2index字典
        """
        num2index = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in num2index:
                another_index = num2index[another_num]
                return [another_index, index]
            num2index[num] = index


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = s.twoSum(nums, target)
    print(res)
