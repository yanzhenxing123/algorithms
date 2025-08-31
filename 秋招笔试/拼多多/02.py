"""
@Time: 2025/8/31 16:31
@Author: yanzx
@Description:
3
1 2 3
==
0 1 2

4
4 2 3 1
==
0 1 1 0

"""

from collections import deque


def min_walks(n, portals):
    # 初始化步行次数，默认无穷大
    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    dq = deque([1])

    while dq:
        u = dq.popleft()

        # 传送门 (代价0)
        v = portals[u - 1]
        if dist[v] > dist[u]:
            dist[v] = dist[u]
            dq.appendleft(v)

        # 步行 (代价1)
        for v in [u - 1, u + 1]:
            if 1 <= v <= n and dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                dq.append(v)

    return dist[1:]


# 读入
if __name__ == "__main__":
    n = int(input().strip())
    portals = list(map(int, input().split()))
    ans = min_walks(n, portals)
    print(" ".join(map(str, ans)))
