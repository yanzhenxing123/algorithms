"""
@Author: yanzx
@Time: 2025/8/26 10:58 
@Description:
01背包: n种物品，每种物品有无数个，每个物品有自己的重量和价值，问容量为m的背包的最大价值

eg:
        重量    价值
物品0     1      15
物品1     3      20
物品2     4      30

背包容量: 4

遍历顺序：
    for 遍历物品
        for 遍历背包容量

二维实现的遍历顺序可以换
d
"""


class Solution:
    def knapsack_complete(self, weights, values, capacity):
        """
        dp[i][j]: 0~i的物品放到容量为j的背包的最大价值
        :param weights:
        :param values:
        :param capacity:
        :return:
        """
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n)]

        # 初始化第一行
        for j in range(weights[0], capacity + 1):
            dp[0][j] = dp[0][j - weights[0]] + values[0]  # 可以放很多个 注意和01的区别

        print(dp)

        """
        
        [[0, 15, 30, 45, 60],
         [0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0]]

        """

        for i in range(1, n):
            for j in range(1, capacity + 1):
                # weight[i] > j 则表示放不下
                if weights[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - weights[i]] + values[i])
        return dp[-1][-1]

    def knapsack_complete_dfs(self, weights, values, capacity):
        """
        使用回溯暴力解
        :param weights:
        :param values:
        :param capacity:
        :return:
        """

        res = 0
        def dfs(weights, values, capacity, index, path_weight, path_value):
            nonlocal res
            if sum(path_weight) <= capacity:
                res = max(res, sum(path_value))
            if sum(path_weight) >= capacity:
                return

            for i in range(index, len(weights)):
                path_weight.append(weights[i])
                path_value.append(values[i])

                dfs(weights, values, capacity, i, path_weight, path_value)
                path_value.pop()
                path_weight.pop()
        dfs(weights, values, capacity, 0, [], [])

        return res


if __name__ == '__main__':
    s = Solution()
    weights = [3, 2, 4]  # 物品重量
    values = [15, 20, 30]  # 物品价值
    capacity = 4  # 背包容量

    # res = s.knapsack_complete(weights, values, capacity)
    # print(res)
    res = s.knapsack_complete_dfs(weights, values, capacity)
    print(res)
