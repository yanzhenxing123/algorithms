"""
@Author: yanzx
@Time: 2025/8/31 16:05 
@Description: 
"""

t = int(input())

for _ in range(t):
    max_time = int(input())
    interval_num = int(input())
    intervals = []
    for _ in range(interval_num):
        a, b = map(int, input().split())
        intervals.append((a, b))

    intervals = sorted(intervals, key=lambda x: x[0])

    res = []
    res.append(intervals[0])
    for interval in intervals[1:]:
        left = res[-1]
        right = interval

        if left[1] < right[0]:
            res.append(right)
        else:
            if left[1] >= right[1]:
                continue
            else:
                new_interval = (left[0], right[1])
                res.pop()
                res.append(new_interval)

    res_ = 0
    for a, b in res:
        res_ += (b - a + 1)

    print(max_time - res_)



