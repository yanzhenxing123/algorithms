"""
@Time: 2025/8/16 10:41
@Author: yanzx
@Description:


6
azbyxb

4
AZaz
"""


def solve():
    # 定义合法字母对
    pairs = set()
    for i in range(13):
        c1 = chr(ord('a') + i)
        c2 = chr(ord('z') - i)
        pairs.add((c1, c2))
        pairs.add((c2, c1))
        pairs.add((c1.upper(), c2.upper()))
        pairs.add((c2.upper(), c1.upper()))

    n = int(input())
    s = input().strip()

    # 破环成链
    extended = s + s
    pos = [0] * (2 * n)
    for i in range(2 * n):
        c = extended[i].lower()
        pos[i] = ord(c) - ord('a') + 1



    # O(n^2)区间DP（只考虑区间两端配对）
    dp = [[0] * (2 * n) for _ in range(2 * n)]
    for length in range(2, n + 1):
        for i in range(2 * n - length + 1):
            j = i + length - 1
            # 不选i或j
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            # 只考虑区间两端配对
            if (extended[i], extended[j]) in pairs:
                left = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                dp[i][j] = max(dp[i][j], left + pos[i] * pos[j])

    max_score = 0
    for i in range(n):
        max_score = max(max_score, dp[i][i + n - 1])
    print(max_score)


solve()