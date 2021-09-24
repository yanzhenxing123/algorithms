"""
@Author: yanzx
@Date: 2021/5/16 17:03
@Description: 
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals.append(newInterval)
            return intervals
        index = 0
        flag = False
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                index = i
                flag = True
                intervals.insert(i, newInterval)
                break
        if not flag:
            intervals.append(newInterval)
            index = len(intervals) - 1

        if index > 0:
            if newInterval[0] <= intervals[index - 1][1] and newInterval[1] > intervals[index - 1][1]:
                tmp = intervals.pop(index - 1)
                newInterval[0] = tmp[0]
                index -= 1
            elif newInterval[0] <= intervals[index - 1][1] and newInterval[1] <= intervals[index - 1][1]:
                intervals.pop(index)
                return intervals

        pop_indexes = []
        for i in range(index + 1, len(intervals)):
            if newInterval[1] >= intervals[i][0] and newInterval[1] >= intervals[i][1]:
                pop_indexes.append(i)
            elif newInterval[1] >= intervals[i][0] and newInterval[1] < intervals[i][1]:
                newInterval[1] = intervals[i][1]
                pop_indexes.append(i)
                break

        for i in pop_indexes[::-1]:
            intervals.pop(i)
        return intervals


if __name__ == '__main__':
    s = Solution()
    intervals = [[2,6],[7,9]]
    newInterval = [17, 19]
    res = s.insert(intervals, newInterval)
    print(res)
