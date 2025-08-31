import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))

        first, last = {}, {}
        for i, v in enumerate(arr):
            if v not in first:
                first[v] = i
            last[v] = i

        vals = sorted(set(arr))
        total = len(vals)

        best = 1
        cur = 1
        for i in range(1, len(vals)):
            # 如果当前值 v 能和前一个值 vals[i-1] 接上
            if vals[i] == vals[i-1] + 1 and last[vals[i-1]] < first[vals[i]]:
                cur += 1
            else:
                cur = 1
            best = max(best, cur)

        ans = total - best
        print(ans)

if __name__ == "__main__":
    solve()
