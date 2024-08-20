"""
@Time: 2024/8/20 16:27
@Author: yanzx
@Desc:
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        找到前边的min_price，计算max_profit
        :param prices:
        :return:
        """
        if len(prices) <= 1:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_profit


if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    res = s.maxProfit(prices)
    print(res)

