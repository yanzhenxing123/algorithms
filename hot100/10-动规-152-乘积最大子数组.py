"""
@Author: yanzx
@Date: 2025/3/4 13:12
@Description:


152. 乘积最大子数组
中等
相关标签
相关企业
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。




示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        res = max(nums[0], -float("inf"))
        for i in range(1, len(nums)):
            res = max(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i], res)
            dp_min[i] = min(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i])
            dp_max[i] = max(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i])
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.maxProduct(nums=[2, -1, 1, 1])
    print(res)
