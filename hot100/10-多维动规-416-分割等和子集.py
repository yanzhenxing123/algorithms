"""

416. 分割等和子集
中等
相关标签
相关企业
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。



示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]

    def canPartition_2nd(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True  # 空子集的和为0

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(target + 1):
                if j < num:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]

        return dp[n][target]


if __name__ == '__main__':
    s = Solution()
