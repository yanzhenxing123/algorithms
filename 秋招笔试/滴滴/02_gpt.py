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

import sys


def solve() -> None:
    t = int(input().strip())  # 输入测试用例数
    out_lines = []

    for _ in range(t):
        n = int(input().strip())  # 每个测试用例的矩阵行数
        a = [list(map(int, input().split())) for _ in range(n)]  # 读取矩阵

        # 用于存储每行的前缀和
        prefix = [[0] * (n + 1) for _ in range(n)]
        row_sum = [0] * n

        # 计算前缀和
        for i in range(n):
            ps = 0
            for j in range(n):
                ps += a[i][j]
                prefix[i][j + 1] = ps
            row_sum[i] = ps

        # 结果变量初始化
        ans = float('-inf')

        # 遍历每一列，并计算跨行的最佳选择
        for c in range(1, n + 1):
            base = prefix[0][c - 1]
            for i in range(n):
                if (i + 1) % 2 == 1:  # 奇数行（1-indexed）
                    tail = row_sum[i] - prefix[i][c - 1]
                else:  # 偶数行（1-indexed）
                    tail = prefix[i][c]
                ans = max(ans, base + tail)

        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines) + "\n")


if __name__ == "__main__":
    solve()


