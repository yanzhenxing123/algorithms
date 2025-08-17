"""
@Time: 2024/3/26 22:46
@Author: yanzx
@Desc:


给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。

在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。

返回插入之后的 intervals。

注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。



示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""

from typing import List


class Solution:
    def merge(self, intervals):
        if not intervals or len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            right = intervals[i]
            left = res[-1]
            if left[1] < right[0]:
                res.append(right)
            else:
                res.pop()
                new_interval = []
                new_interval.append(left[0])
                if left[1] < right[1]:
                    new_interval.append(right[1])
                else:
                    new_interval.append(left[1])
                res.append(new_interval)
        return res

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals.append(newInterval)
            return intervals
        if newInterval[0] <= intervals[0][0]:
            intervals_to_merge = [newInterval] + intervals
            res = self.merge(intervals_to_merge)
            return res
        if newInterval[0] >= intervals[-1][0]:
            intervals_to_merge = intervals + [newInterval]
            res = self.merge(intervals_to_merge)
            return res

        for i, j in zip(range(0, len(intervals) - 1), range(1, len(intervals))):
            if intervals[i][0] <= newInterval[0] and newInterval[0] <= intervals[j][0]:
                break

        left_intervals = intervals[:i]
        intervals_to_merge = [intervals[i]] + [newInterval] + intervals[j:]
        right_intervals = self.merge(intervals_to_merge)
        return left_intervals + right_intervals


if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    # 输出：[[1, 2], [3, 10], [12, 16]]
    res = s.insert(intervals, newInterval)
    print(res)
