import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))

        first = {}
        last = {}
        for i, v in enumerate(arr):
            if v not in first:
                first[v] = i
            last[v] = i

        vals = sorted(set(arr))  # 不同的值，升序
        dp = {}
        best = 0
        for i, v in enumerate(vals):
            dp[v] = 1  # 至少自己单独一类
            if i > 0:
                u = vals[i-1]
                if last[u] < first[v]:
                    dp[v] = dp[u] + 1
            best = max(best, dp[v])

        ans = len(vals) - best
        print(ans)

if __name__ == "__main__":
    solve()
