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

        ans = 0
        pref_row1 = prefix[0]
        for c in range(1, n + 1):
            base = pref_row1[c - 1]
            for i in range(n):
                pref_i = prefix[i]
                if (i + 1) & 1:
                    tail = row_sum[i] - pref_i[c - 1]
                else:
                    tail = pref_i[c]
                total = base + tail
                if total > ans:
                    ans = total

        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()


