"""
@Time: 2024/3/26 22:46
@Author: yanzx
@Desc:


以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].


按照第一个间排序 然后合并即可
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        按照第一个key排序再合并，简单题
        :param intervals:
        :return:
        """
        if not intervals:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            interval_left = res[-1]
            interval_right = intervals[i]
            if interval_left[1] >= interval_right[0]:  # 合并
                if interval_left[1] >= interval_right[1]:
                    continue
                else:
                    res.pop()
                    res.append([interval_left[0], interval_right[1]])
            else:
                res.append(interval_right)
        return res


if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = s.merge(intervals)
    print(res)
