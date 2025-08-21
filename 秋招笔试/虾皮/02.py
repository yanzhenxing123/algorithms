"""
@Author: yanzx
@Time: 2025/8/20 17:11 
@Description:


def optimal_container_selection(W, w):
    n = len(w)
    # dp[i][j] 表示前i个集装箱中总重量为j时的最小集装箱数量
    # 初始化为无穷大，表示不可达
    dp = [[float('inf')] * (W + 1) for _ in range(n + 1)]
    # selected[i][j] 表示前i个集装箱中总重量为j时选择的集装箱情况
    selected = [[None] * (W + 1) for _ in range(n + 1)]

    # 初始化，总重量为0时不需要任何集装箱
    for i in range(n + 1):
        dp[i][0] = 0
        selected[i][0] = [0] * n

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # 不选第i个集装箱
            dp[i][j] = dp[i-1][j]
            selected[i][j] = selected[i-1][j]

            # 选第i个集装箱
            if j >= w[i-1] and dp[i-1][j-w[i-1]] + 1 < dp[i][j]:
                dp[i][j] = dp[i-1][j-w[i-1]] + 1
                new_selected = selected[i-1][j-w[i-1]].copy()
                new_selected[i-1] = 1
                selected[i][j] = new_selected

    if dp[n][W] == float('inf'):
        return [0] * n  # 无解时返回全0

    return selected[n][W]

# 示例1
W = 10
w = [5, 2, 6, 4, 3]
print(optimal_container_selection(W, w))  # 输出: [0, 0, 1, 1, 0]
"""


#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
#
# @param w int整型  卡车的载重量
# @param c int整型 一维数组 每个集装箱的重量
# @return int整型一维数组
#
class Solution:
    def trunkLoad(self, w, c):
        # write code here
        W = w
        w = c
        n = len(w)
        # dp[i][j] 表示前i个集装箱中总重量为j时的最小集装箱数量
        # 初始化为无穷大，表示不可达
        dp = [[float('inf')] * (W + 1) for _ in range(n + 1)]
        # selected[i][j] 表示前i个集装箱中总重量为j时选择的集装箱情况
        selected = [[None] * (W + 1) for _ in range(n + 1)]

        # 初始化，总重量为0时不需要任何集装箱
        for i in range(n + 1):
            dp[i][0] = 0
            selected[i][0] = [0] * n

        for i in range(1, n + 1):
            for j in range(1, W + 1):
                # 不选第i个集装箱
                dp[i][j] = dp[i - 1][j]
                selected[i][j] = selected[i - 1][j]

                # 选第i个集装箱
                if j >= w[i - 1] and dp[i - 1][j - w[i - 1]] + 1 < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - w[i - 1]] + 1
                    new_selected = selected[i - 1][j - w[i - 1]].copy()
                    new_selected[i - 1] = 1
                    selected[i][j] = new_selected

        if dp[n][W] == float('inf'):
            return [0] * n  # 无解时返回全0

        return selected[n][W]


if __name__ == '__main__':
    w = 10
    c = [5, 2, 6, 4, 3]
    s = Solution()
    res = s.trunkLoad(w, c)
    print(res)
