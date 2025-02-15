"""
@Time: 2024/3/24 15:47
@Author: yanzx
@Desc:
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

height = [4,2,0,3,2,5]
输出：9
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        如何去除空间复杂度的O(n)，使得空间复杂度为O(1)
        即：左右两边知道left_max和right_max，取其中小的，肯定就是当前的min(left_max, right_max)，直接计算即可
        :param height:
        :return:
        """
        if not height:
            return 0
        res = 0
        left_max = height[0]
        right_max = height[-1]
        left, right = 0, len(height) - 1
        while left < right:
            if left_max <= right_max:
                res += left_max - height[left]
                left += 1
                left_max = max(height[left], left_max)
            else:
                res += right_max - height[right]
                right -= 1
                right_max = max(height[right], right_max)
        return res

    def trap2(self, height: List[int]) -> int:
        """
        获取此点的左边最大和右边最大，如果自身大就是自己，然后取min做减法
        :param height:
        :return:
        """
        if not height:
            return 0
        res = 0
        left_max_arr = [height[0]] + [0 for _ in range(len(height) - 1)]
        right_max_arr = [0 for _ in range(len(height) - 1)] + [height[-1]]
        for i in range(1, len(height)):  # 从做到右
            left_max_arr[i] = max(height[i], left_max_arr[i - 1])
        for j in range(len(height) - 2, -1, -1):
            right_max_arr[j] = max(height[j], right_max_arr[j + 1])

        print(left_max_arr)
        print(right_max_arr)
        for k in range(len(height)):
            res += min(left_max_arr[k], right_max_arr[k]) - height[k]
        return res


if __name__ == '__main__':
    s = Solution()
    height = [4, 2, 0, 3, 2, 5]
    res = s.trap2(height)
    print(res)
