"""
@Time: 2025/8/26 19:22
@Author: yanzx
@Description:

2
3
2 4 5
2
3 2

=> 2 0

"""

import heapq


def min_operations():
    T = int(input())
    for _ in range(T):

        n = int(input())
        a = list(map(int, input().split()))
        original_first = a[0]
        max_heap = []
        for num in a[1:]:
            heapq.heappush(max_heap, -num)  # 用最大堆来维护其他元素

        operations = 0
        while True:
            if not max_heap:
                break
            current_max = -max_heap[0]
            if original_first > current_max:
                break
            # 需要操作
            x = current_max // 2
            original_first += x
            new_val = current_max - x
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -new_val)
            operations += 1
        print(operations)


min_operations()