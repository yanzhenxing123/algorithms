import sys
input = sys.stdin.readline
MOD = 10**9 + 7

def solve():
    n, m = map(int, input().split())
    s = input().strip()

    # 预处理 26^k
    pow26 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow26[i] = (pow26[i - 1] * 26) % MOD

    # 计算每个字母的贡献
    contrib = [0] * 26
    for i, ch in enumerate(s):
        c = ord(ch) - ord('a')
        contrib[c] = (contrib[c] + pow26[n - 1 - i]) % MOD

    for _ in range(m):
        b = list(map(int, input().split()))  # b[0] 对应 'a'
        ans = 1
        for c in range(26):
            smaller = b[c] - 1
            ans = (ans + smaller * contrib[c]) % MOD
        print(ans)

if __name__ == "__main__":
    solve()
