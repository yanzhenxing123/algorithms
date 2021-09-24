"""
@Author: yanzx
@Date: 2021/5/14 23:37
@Description: 
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] > intervals[i][0] and res[-1][1] < intervals[i][1]:
                res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        return res


if __name__ == '__main__':
    intervals = [[1, 3], [-1, 6], [8, 10], [15, 18]]
    s = Solution()
    res = s.merge(intervals)
    print(res)
