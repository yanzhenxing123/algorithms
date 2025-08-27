"""
@Time: 2024/4/29 14:17
@Author: yanzx
@Desc: 柱状图中最大的矩形

使用的方法也是单调栈，不会做，太难了


问题描述
给定一个数组 heights，表示柱状图的高度，求其中能画出的最大矩形的面积。
算法思路
1. 单调栈的核心思想
维护一个单调递增的栈
栈中存储的是索引，对应的柱高是递增的
当遇到一个比栈顶柱高矮的柱子时，说明找到了栈顶柱子的右边界
2. 关键步骤分析

初始：heights = [0, 2, 1, 5, 6, 2, 3, 0]


i=0: heights[0]=0, stack=[0]
i=1: heights[1]=2, stack=[0,1]  (2>0, 入栈)
i=2: heights[2]=1, heights[1]=2>1
      - 弹出1，计算面积：(2-0-1)*2 = 1*2 = 2
      - stack=[0,2] (1入栈)
i=3: heights[3]=5, stack=[0,2,3] (5>1, 入栈)
i=4: heights[4]=6, stack=[0,2,3,4] (6>5, 入栈)
i=5: heights[5]=2, heights[4]=6>2
      - 弹出4，计算面积：(5-3-1)*6 = 1*6 = 6
      - 弹出3，计算面积：(5-2-1)*5 = 2*5 = 10
      - stack=[0,2,5] (2入栈)
i=6: heights[6]=3, stack=[0,2,5,6] (3>2, 入栈)
i=7: heights[7]=0, 处理所有剩余柱子...
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)

        return res

    def largestRectangleArea_暴力(self, heights: List[int]) -> int:
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
