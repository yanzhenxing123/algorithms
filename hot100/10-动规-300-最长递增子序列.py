"""
@Author: yanzx
@Date: 2025/3/4 10:57
@Description:

300. 最长递增子序列

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1


[0, 1, 0, 3, 2, 3]
[0, 1, 0, 3, 2, 3]
[0, 1, 0, 3, 2, 3]
[0, 1, 0, 3, 2, 3]
[0, 1, 0, 3, 2, 3]





"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        两个循环，检查当前数字是否比之前的数字大，然后
        :param nums:
        :return:
        """
        if not nums:
            return 0
        dp = [1] * len(nums) # dp[i] 到当前位置最长严格递增子序列的长度
        res = 1
        for i in range(1, len(nums)):
            for j in range(0, i):  # 下三角进行遍历
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
            res = max(dp[i], res)
            print(dp)
        return res

    def lengthOfLIS_2nd(self, nums: List[int]) -> int:
        """
        固定当前值，检查之前的值，也就是下三角遍历
        :param nums:
        :return:
        """
        if not nums:
            return 0
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 2, 1]
    s = Solution()
    res = s.lengthOfLIS(nums)
    print(res)
