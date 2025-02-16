"""
@Time: 2024/3/26 22:37
@Author: yanzx
@Desc:
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和子数组是数组中的一个连续部分。
示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

dp = [-2, 1, -2, 4, 3, 5, 6, 1, 5]
到这个nums[i]的时候前面子串的最大值

动态规划 dp[i] = max(dp[i-1] + nums[i], nums[i])
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(nums[i], dp[-1] + nums[i]))
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = s.maxSubArray(nums)
    print(res)