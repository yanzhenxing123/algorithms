"""
@Author: yanzx
@Date: 2021-10-24 11:04:21
@Desc: 
"""

from itertools import permutations

n = int(input())

res = permutations(list(range(1, n+1)), n)
for i in res:
    for j in i:
        print(j, end=' ')
    print()