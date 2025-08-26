"""

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
import sys

def solve() -> None:
    t = int(input().strip())  # 输入测试用例数
    out_lines = []

    for _ in range(t):
        n = int(input().strip())  # 每个测试用例的矩阵行数
        a = [list(map(int, input().split())) for _ in range(n)]  # 读取矩阵

        # dp[i][j] 代表在第 i 行选择第 j 列时的最大路径值
        dp = [[-float('inf')] * n for _ in range(n)]  # 初始化为负无穷

        # 初始化第一行的 dp 为第一行的值
        for j in range(n):
            dp[0][j] = a[0][j]

        # 动态规划填充 dp 数组
        for i in range(1, n):
            for j in range(n):
                # 从上一行的 j-1 或 j+1 列选择最大值来更新当前行
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a[i][j])
                if j < n - 1:
                    dp[i][j] = max(dp[i][j], dp[i-1][j+1] + a[i][j])

        # 从最后一行选择最大值
        ans = max(dp[n-1])

        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()


