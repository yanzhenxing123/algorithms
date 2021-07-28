"""
@Author: yanzx
@Date: 2021-07-28 11:13:42
@Desc: 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums中可能有重复的数字 遍历一次即可 注意：enumerate得到(index, value)
        hashmap = {}
        for index, num in enumerate(nums):
            another = target - num
            if another in hashmap:
                return [index, hashmap[another]]
            hashmap[num] = index


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = s.twoSum(nums, target)
    print(res)
