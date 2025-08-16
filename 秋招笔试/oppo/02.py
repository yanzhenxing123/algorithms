"""
@Time: 2025/8/16 10:26
@Author: yanzx
@Description:


5
3
1 2 4
3
1 2 6
1
1
2
1 536870911
5
25752 3010 1188 126 270

"""

import sys
import bisect
from collections import defaultdict


def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))

        freq = defaultdict(int)
        for num in a:
            x = num
            while x > 0:
                freq[x] += 1
                x = x // 2

        possible = True
        for k in range(n, 0, -1):
            if freq[k] == 0:
                possible = False
                break
            freq[k] -= 1
            x = k // 2
            while x > 0:
                if freq[x] > 0:
                    freq[x] -= 1
                x = x // 2

        print("YES" if possible else "NO")


solve()