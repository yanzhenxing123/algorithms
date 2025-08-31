import sys
import bisect

input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))

        # 记录不同值的第一次出现顺序
        first_pos = {}
        seq = []
        for i, v in enumerate(arr):
            if v not in first_pos:
                first_pos[v] = i
                seq.append(v)

        # 对seq求最长非降子序列 (因为值大小也影响顺序)
        # 注意这里seq是不同值的出现顺序，但我们要求按值大小非降
        # 所以真正的序列是 [值1, 值2, ...]
        lis = []
        for v in seq:
            pos = bisect.bisect_right(lis, v)
            if pos == len(lis):
                lis.append(v)
            else:
                lis[pos] = v

        longest = len(lis)
        ans = len(seq) - longest
        print(ans)

if __name__ == "__main__":
    solve()
