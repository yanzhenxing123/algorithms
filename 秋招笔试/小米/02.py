def solve():
    try:
        T = int(input().strip())
    except Exception:
        return
    out = []
    INF = 10**18
    for _ in range(T):
        n, m = map(int, input().strip().split())
        a = [list(map(int, input().strip().split())) for __ in range(n)]
        dp = [[INF]*(m+1) for _ in range(n+1)]
        dp[n][m-1] = 1
        dp[n-1][m] = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                need_next = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, need_next - a[i][j])
        out.append(str(dp[0][0]))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
