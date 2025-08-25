"""
@Time: 2024/8/20 16:27
@Author: yanzx
@Desc:



122. 买卖股票的最佳时机 II

给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。



示例 1：

输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3。
最大总利润为 4 + 3 = 7 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
最大总利润为 4 。
示例 3：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0。



输入：prices = [7,1,5,3,6,4]

[[0, -7],
[0, -1],
[4, -1],
[4, 1],
[7, 1],
[7, 3]]

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        print("DP状态定义:")
        print("dp[i][0]: 第i天结束时，不持有股票的最大利润")
        print("dp[i][1]: 第i天结束时，持有股票的最大利润")
        print()
        print("状态转移:")
        print("dp[i][0] = max(不操作, 卖出股票)")
        print("dp[i][1] = max(不操作, 买入股票)")



        transitions = {
            "dp[i][0] (不持有股票)": [
                "dp[i-1][0]: 前一天就不持有，今天也不持有",
                "dp[i-1][1] + prices[i]: 前一天持有，今天卖出"
            ],
            "dp[i][1] (持有股票)": [
                "dp[i-1][1]: 前一天就持有，今天继续持有",
                "dp[i-1][0] - prices[i]: 前一天不持有，今天买入"
            ]
        }

        :param prices:
        :return:
        """
        if len(prices) <= 1:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]

        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(
                dp[i - 1][0],
                dp[i - 1][1] + prices[i]
            )
            dp[i][1] = max(
                dp[i - 1][1],
                dp[i - 1][0] - prices[i]
            )
        print(dp)

        return dp[len(prices) - 1][0]

if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    res = s.maxProfit(prices)
    print(res)

