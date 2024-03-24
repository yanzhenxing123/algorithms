"""
@Time: 2024/3/23 09:47
@Author: yanzx
@Desc:
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。


输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        解题思路：双指针 left, right：取完area之后，让矮的那个移动 移动到比自己之前大的地方
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

    def maxArea2(self, height: List[int]) -> int:
        """
        最大区域
        O(n^2) 超出了时间复杂度
        :param height:
        :return:
        """
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                h = min(height[i], height[j])
                w = j - i
                area = h * w
                if area > max_area:
                    max_area = area

        return max_area


if __name__ == '__main__':
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # height = [1, 1]
    res = s.maxArea(height)
    print(res)
