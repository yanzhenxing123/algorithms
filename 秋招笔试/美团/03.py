import heapq


def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    INF = float('inf')
    dist = [[INF] * (k + 1) for _ in range(n + 1)]
    dist[1][k] = 0
    heap = []
    heapq.heappush(heap, (0, 1, k))

    while heap:
        current_dist, u, remaining = heapq.heappop(heap)

        # 如果当前距离已经不是最优，跳过
        if current_dist > dist[u][remaining]:
            continue

        for v, w in adj[u]:
            if a[v - 1] >= 0:
                # 强制增加坏魔法石的时间
                new_dist = current_dist + w + a[v - 1]
                if new_dist < dist[v][remaining]:
                    dist[v][remaining] = new_dist
                    heapq.heappush(heap, (new_dist, v, remaining))
            else:
                # 不使用好魔法石
                new_dist = current_dist + w
                if new_dist < dist[v][remaining]:
                    dist[v][remaining] = new_dist
                    heapq.heappush(heap, (new_dist, v, remaining))

                # 使用好魔法石
                if remaining > 0:
                    new_dist = current_dist + w + a[v - 1]
                    new_remaining = remaining - 1
                    if new_dist < dist[v][new_remaining]:
                        dist[v][new_remaining] = new_dist
                        heapq.heappush(heap, (new_dist, v, new_remaining))

    # 找到到达城市 n 的最小距离
    answer = min(dist[n])
    if answer == INF:
        print("NO")
    else:
        print(answer)


# 调试信息
if __name__ == "__main__":
    solve()