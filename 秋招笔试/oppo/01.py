import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        threshold = (n + 1) // 2  # 上取整

        # 初始频率统计
        freq = [0] * (n + 1)
        for v in arr:
            freq[v] += 1
        max_freq = max(freq)

        ans = 0
        if max_freq >= threshold:
            ans += 1  # 初始状态满足

        # 处理 m 次修改
        for _ in range(m):
            x, y = map(int, input().split())
            x -= 1  # 下标从0开始
            old = arr[x]
            new = y
            if old == new:
                # 无变化，直接看当前是否满足
                if max_freq >= threshold:
                    ans += 1
                continue

            # 更新频率
            freq[old] -= 1
            freq[new] += 1
            arr[x] = new

            # 更新 max_freq
            if freq[new] > max_freq:
                max_freq = freq[new]
            elif freq[old] + 1 == max_freq and freq[old] < max_freq:
                # 如果减少的是原来的最大值，需要重新计算
                max_freq = max(freq)

            # 判断
            if max_freq >= threshold:
                ans += 1

        print(ans)

if __name__ == "__main__":
    solve()
