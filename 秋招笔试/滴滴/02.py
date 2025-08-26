"""
@Time: 2025/8/26 19:33
@Author: yanzx
@Description:

2
3
1 2 3
4 5 6
7 8 9
2
0 5
3 1

==
24
5

"""


def main():
    T = int(input().strip())
    results = []

    for _ in range(T):
        n = int(input().strip())
        grid = []
        for i in range(n):
            row = list(map(int, input().split()))
            grid.append(row)

        # dp[i][j][0]: 到达(i,j)但不带走宝藏的最大价值
        # dp[i][j][1]: 到达(i,j)并带走宝藏的最大价值
        dp0 = [[-10 ** 9] * n for _ in range(n)]
        dp1 = [[-10 ** 9] * n for _ in range(n)]

        # 初始化起点
        dp0[0][0] = 0  # 在起点不带走宝藏
        dp1[0][0] = grid[0][0]  # 在起点带走宝藏

        # 动态规划
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                # 从上方转移（向下移动）
                if i > 0:
                    # 从上方下来但不带走当前宝藏
                    from_above_skip = max(dp0[i - 1][j], dp1[i - 1][j])
                    # 从上方下来并带走当前宝藏
                    from_above_take = max(dp0[i - 1][j], dp1[i - 1][j]) + grid[i][j]

                    dp0[i][j] = max(dp0[i][j], from_above_skip)
                    dp1[i][j] = max(dp1[i][j], from_above_take)

                # 从左边转移（向右移动，必须左边带走了宝藏）
                if j > 0:
                    from_left = dp1[i][j - 1] + grid[i][j]
                    dp1[i][j] = max(dp1[i][j], from_left)

        # 最终答案：所有可能出口的最大值
        max_val = 0
        for j in range(n):
            max_val = max(max_val, dp0[n - 1][j], dp1[n - 1][j])
        for i in range(n):
            max_val = max(max_val, dp0[i][n - 1], dp1[i][n - 1])

        results.append(str(max_val))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()