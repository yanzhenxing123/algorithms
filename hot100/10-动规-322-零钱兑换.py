"""
@Author: yanzx
@Date: 2025/3/4 10:30
@Description:

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1


示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0


其实就是背包问题，无限次的拿，问装满这个背包最少需要多少件物品？

dp[j]: 表示装满容量为j的背包需要的最少物品的数量

"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 先遍历物品，再遍历背包
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
                print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange_2nd(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins or min(coins) > amount:
            return -1
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j-coin] + 1, dp[j])
        if dp[-1] != float('inf'):
            return dp[-1]
        else:
            return -1




if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    s = Solution()
    res = s.coinChange(coins, amount)
    print(res)
