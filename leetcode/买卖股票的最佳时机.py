"""
@Author: yanzx
@Date: 2021/3/22 15:53
@Description:
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0

动态规划问题

prices = [7,1,5,3,6,4]

考虑prices的长度为1时，则返回0

当prices的长度大于1时，设最大利润为：max，最小买入为min

则从索引为1时开始 max = 0, min = prices[0]

然后 max = max(max, cur - min)
     min = min(min, cur)

"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_profit = 0
        min_input = prices[0]

        for cur in prices:
            max_profit = max(max_profit, cur - min_input)
            min_input = min(min_input, cur)

        return max_profit


if __name__ == '__main__':
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    res = s.maxProfit(prices)
    print(res)




