"""
@Time: 2025/9/6 16:15
@Author: yanzx
@Description: 
"""

import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    try:
        T = int(next(it))
    except StopIteration:
        return
    out_lines = []

    for _ in range(T):
        n = int(next(it)); m = int(next(it))
        xs = [int(next(it)) for _ in range(m)]
        ys = [int(next(it)) for _ in range(m)]

        # Use a set to deduplicate pairs and handle possible duplicates
        edges = set()
        for x, y in zip(xs, ys):
            x -= 1; y -= 1
            if x == y:
                edges.add((x, y))
            else:
                if x > y:
                    x, y = y, x
                edges.add((x, y))

        ALL = (1 << n) - 1
        diff = [0] * n  # bitset of nodes different from i
        for x, y in edges:
            if 0 <= x < n and 0 <= y < n:
                diff[x] |= (1 << y)
                diff[y] |= (1 << x)

        # equal[i] are nodes judged same as i (excluding i)
        equal = [0] * n
        for i in range(n):
            equal[i] = (ALL ^ diff[i]) & ~(1 << i)

        ok = True
        for u, v in edges:
            if (equal[u] & equal[v]) != 0:
                ok = False
                break

        out_lines.append("Yes" if ok else "No")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
