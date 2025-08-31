"""
@Time: 2025/8/31 17:52
@Author: yanzx
@Description: 
"""

import sys
from collections import defaultdict


def solve():
    ptr = 0
    T = int(input())
    ptr += 1
    for _ in range(T):
        n = int(input())
        ptr += 1
        a = list(map(int, input().split()))
        ptr += n

        # 记录每个数字的所有出现位置（0-based）
        num_pos = defaultdict(list)
        for idx, num in enumerate(a):
            num_pos[num].append(idx)

        # 所有唯一的数字，并排序
        unique_nums = sorted(num_pos.keys())
        m = len(unique_nums)
        if m == 0:
            print(0)
            continue

        max_len = 1
        current_len = 1
        for i in range(1, m):
            prev_num = unique_nums[i - 1]
            current_num = unique_nums[i]
            # 检查current_num的所有位置是否都大于prev_num的所有位置
            if num_pos[current_num][0] > num_pos[prev_num][-1]:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
        print(m - max_len)


solve()