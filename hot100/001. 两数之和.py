"""
@Time: 2024/3/22 22:47
@Author: yanzx
@Desc: 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        hashmap
        :param nums:
        :param target:
        :return:
        """
        # nums中可能有重复的数字 遍历一次即可 注意：enumerate得到(index, value)
        hashmap = {}
        for index, num in enumerate(nums):
            another = target - num
            hashmap[num] = index
            if another in hashmap:
                return [index, hashmap[another]]



if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = s.twoSum(nums, target)
    print(res)
