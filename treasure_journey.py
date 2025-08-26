import sys


def solve() -> None:

    try:
        t = int(input().strip())
    except Exception:
        return
    out_lines = []
    for _ in range(t):
        n = int(input().strip())
        a = [list(map(int, input().split())) for _ in range(n)]

        prefix = [[0] * (n + 1) for _ in range(n)]
        row_sum = [0] * n
        for i in range(n):
            ps = 0
            pref_i = prefix[i]
            row_i = a[i]
            for j in range(n):
                ps += row_i[j]
                pref_i[j + 1] = ps
            row_sum[i] = ps

        # 新建模：每列必须向右恰好一次，竖直方向只允许向下（行号非递减）
        # 等价于：在每一列 j 选择一个行 i_j，要求 i_1 <= i_2 <= ... <= i_n，收益是 sum a[i_j][j]
        # 这是经典的前缀最大 DP。
        dp_prev = [a[i][0] for i in range(n)]
        for j in range(1, n):
            best = -1
            dp_cur = [0] * n
            for i in range(n):
                if dp_prev[i] > best:
                    best = dp_prev[i]
                dp_cur[i] = best + a[i][j]
            dp_prev = dp_cur
        ans = max(dp_prev)

        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()


