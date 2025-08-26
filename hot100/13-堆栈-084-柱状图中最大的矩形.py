"""
@Time: 2024/4/29 14:17
@Author: yanzx
@Desc: 柱状图中最大的矩形

使用的方法也是单调栈，不会做，太难了
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        暴力解决方法
        :param heights:
        :return:
        """
        max_res = 0
        for i in range(len(heights)):
            height = heights[i]
            for j in range(i, len(heights)):
                height = min(height, heights[j])
                area = (j - i + 1) * height
                max_res = max(max_res, area)
        return max_res


if __name__ == '__main__':
    s = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    res = s.largestRectangleArea(heights)
    print(res)
