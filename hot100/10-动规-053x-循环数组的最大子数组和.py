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


# 非常简单的一道题
"""

from typing import List


class Solution:
    def kadane(self, nums: List[int]) -> int:
        """
        这种算法叫kadane算法
        :param nums:
        :return:
        """
        if not nums:
            return 0
        dp = [nums[0]]
        res = nums[0]
        for i in range(1, len(nums)):
            dp.append(max(nums[i], dp[-1] + nums[i]))
            res = max(dp[-1], res)

        return res

    def max_circular_sub_sum(self, arr):
        """
        找到循环数组中的最大子数组和

        核心思想：对于跨越边界的部分，最大子数组和 = 总和 - 不跨越边界的最小子数组和

        不跨越边界的最小子数组和: 先对数组取负，然后利用kadane得到最小子数组和的的相反数

        :param arr:
        :return:
        """
        # 情况1：普通的最大子数组和（不跨越边界）
        max_kadane = self.kadane(arr)

        # 情况2：跨越边界的最大子数组和
        # 计算数组总和
        arr_sum = sum(arr)

        # 关键技巧：将数组取负，然后求最大子数组和
        # 这样得到的是原数组最小子数组和的相反数 ⭐️
        arr_neg = [-x for x in arr]
        max_neg_kadane = self.kadane(arr_neg)  # 最小子数组和的相反数

        # 跨越边界的最大和 = 总和 - 最小子数组和
        max_wrap = arr_sum + max_neg_kadane

        # 处理特殊情况：所有元素都为负数
        if max_wrap == 0:
            return max_kadane

        # 返回两种情况的最大值
        return max(max_kadane, max_wrap)


if __name__ == '__main__':
    s = Solution()
    nums = [5, -3, 5]
    res = s.max_circular_sub_sum(nums)
    print(res)
