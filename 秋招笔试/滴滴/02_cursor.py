"""

2
3
1 2 3
4 5 6
7 8 9
2
0 5
3 1
"""
import sys


def solve() -> None:

    try:
        t = int(input().strip())
    except Exception:
        return
    out_lines = []
    for _ in range(t):
        n = int(input().strip())
        a = [[0] * n for _ in range(n)]
        for i in range(n):
            row = list(map(int, input().split()))
            for j in range(n):
                a[i][j] = row[j]

        prefix = [[0] * (n + 1) for _ in range(n)]
        row_sum = [0] * n
        for i in range(n):
            ps = 0
            for j in range(n):
                ps += a[i][j]
                prefix[i][j + 1] = ps
            row_sum[i] = ps

        ans = 0
        for c in range(1, n + 1):
            # 在第一行，只能在到达列 c 之前经过房间的对外门
            base = prefix[0][c - 1]

            for i in range(n):
                row_idx = i
                if (i + 1) % 2 == 1:
                    # 奇数行向右：经过 c..n 的对外门
                    tail = row_sum[row_idx] - prefix[row_idx][c - 1]
                else:
                    # 偶数行向左：经过 1..c 的对外门
                    tail = prefix[row_idx][c]
                total = base + tail
                if total > ans:
                    ans = total

        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()


