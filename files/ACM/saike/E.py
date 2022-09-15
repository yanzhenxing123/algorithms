"""
@Author: yanzx
@Date: 2022/3/27 10:17
@Description: 
"""

k, n = list(map(int, input().split()))

for i in range(n):
    count = k // 10
    if count > 5:
        count = 5
    k += count
    k += 5
print(k)