"""
@Author: yanzx
@Date: 2021/5/16 10:44
@Description: 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(nums[i], dp[-1] + nums[i]))
        print(dp)
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))