"""
@Time: 2025/8/17 20:00
@Author: yanzx
@Description:

5 2
0 2 -5 4 -3
"""

import sys


def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]

    from collections import defaultdict
    count = defaultdict(int)
    count[0] = 1  # prefix[0] = 0

    res = 0
    max_stack = []
    left = [0] * (n + 1)
    right = [n + 1] * (n + 1)

    # Calculate left boundaries
    for i in range(1, n + 1):
        while max_stack and prefix[max_stack[-1]] < prefix[i]:
            max_stack.pop()
        left[i] = max_stack[-1] if max_stack else 0
        max_stack.append(i)

    max_stack = []
    # Calculate right boundaries
    for i in range(n, 0, -1):
        while max_stack and prefix[max_stack[-1]] <= prefix[i]:
            max_stack.pop()
        right[i] = max_stack[-1] if max_stack else n + 1
        max_stack.append(i)

    # Count intervals where max(prefix[l..r]) = k
    for i in range(1, n + 1):
        if prefix[i] == k:
            res += (i - left[i]) * (right[i] - i)

    print(res)


# solve()

import sys

import sys


def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]

    from collections import defaultdict
    count = defaultdict(int)
    count[0] = 1  # prefix[0] = 0

    res = 0
    max_stack = []
    left = [0] * (n + 1)
    right = [n + 1] * (n + 1)

    # Calculate left boundaries
    for i in range(1, n + 1):
        while max_stack and prefix[max_stack[-1]] < prefix[i]:
            max_stack.pop()
        left[i] = max_stack[-1] if max_stack else 0
        max_stack.append(i)

    max_stack = []
    # Calculate right boundaries
    for i in range(n, 0, -1):
        while max_stack and prefix[max_stack[-1]] <= prefix[i]:
            max_stack.pop()
        right[i] = max_stack[-1] if max_stack else n + 1
        max_stack.append(i)

    # Count intervals where max(prefix[l..r]) = k
    for i in range(1, n + 1):
        if prefix[i] == k:
            res += (i - left[i]) * (right[i] - i)

    print(res)


solve()


