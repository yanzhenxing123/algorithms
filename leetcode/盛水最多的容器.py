"""
@Author: yanzx
@Date: 2021/4/18 15:00
@Description: 盛水最多的容器
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0
        while l < r:
            max_area = max(min(height[l], height[r]) * (r - l), max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area



if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    res  =s.maxArea(height)
    print(res)
