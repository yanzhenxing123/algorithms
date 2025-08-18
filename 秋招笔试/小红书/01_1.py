import sys

def solve():
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n, d = map(int, input().split())
        arr = list(map(int, input().split()))
        arr.sort()

        keep = 1  # 至少能保留第一个
        last = arr[0]
        for i in range(1, n):
            if arr[i] - last > d:
                keep += 1
                last = arr[i]
            # 否则 arr[i] 与 last 冲突 -> 舍弃 arr[i]

        print(keep)

if __name__ == "__main__":
    solve()
