"""
@Author: yanzx
@Date: 2021-12-01 20:47:22
@Desc:

给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

两个数组进行异或操作

"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    pass
