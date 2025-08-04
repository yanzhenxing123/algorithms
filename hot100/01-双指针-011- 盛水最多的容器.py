"""
11. 盛最多水的容器
已解答
中等
相关标签
相关企业
提示
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        解题思路：双指针 left, right：取完area之后，让矮的那个移动，且找到一个比当前h大的柱子
        :param height:
        :return:
        """
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            area = h * (right - left)
            if area > max_area:
                max_area = area
            if height[left] >= height[right]:  # right一直往左
                while left < right and height[right] <= h:
                    right -= 1
            else:  # left一直往右
                while left < right and height[left] <= h:
                    left += 1
        return max_area

    def maxArea_2(self, height: List[int]) -> int:
        """
        maxArea_2
        :param height:
        :return:
        """
        if not height or len(height) == 1:
            return 0
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            cur_area = (right - left) * min(height[left], height[right])
            max_area = max(cur_area, max_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
