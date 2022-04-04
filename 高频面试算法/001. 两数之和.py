"""
@Author: yanzx
@Date: 2022/4/3 22:11
@Description:  1. 两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            another = target - nums[i]
            # 先找再放
            if another in data:
                return [i, data[another]]
            data[nums[i]] = i

        return None


if __name__ == '__main__':
    pass