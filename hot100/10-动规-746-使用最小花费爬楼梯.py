"""
@Time: 2024/8/21 22:22
@Author: yanzx
@Desc:
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        1. dp数组：dp[i]代表到达这个楼梯最小的花费, 长度为 n + 1
        2. 状态转移公式：dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        3. 初始化：dp[0] = dp[1] = 0
        4. 遍历顺序：从2开始 往后
        5. 打印数组：[0, 0, 1, 2, 2, 3, 3, 4, 4, 5, 6]
        :param cost:
        :return:
        """
        if len(cost) <= 2:
            return min(cost)
        dp = [0] * (len(cost) + 1)  # 到此阶梯花费的最少钱
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    s = Solution()
    res = s.minCostClimbingStairs(cost)
    print(res)
