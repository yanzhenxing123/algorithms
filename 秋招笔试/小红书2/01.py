"""
@Time: 2025/8/24 19:18
@Author: yanzx
@Description:


5
1 2 3 2 6
==> 2


4
2 4 9 6
"""




def func(n, a):
    max_a = 100
    dp = [0] * (max_a + 1)
    for g in range(2, max_a + 1):
        prev = -1
        for i in range(n):
            if a[i] % g == 0:
                if prev == -1 or i - prev > 1:
                    dp[g] += 1
                    prev = i
    return max(dp)


n = int(input())
a = list(map(int, input().split()))
print(func(n, a))