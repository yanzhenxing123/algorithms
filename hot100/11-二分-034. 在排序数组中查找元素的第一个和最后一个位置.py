"""
@Time: 2024/4/26 11:15
@Author: yanzx
@Desc:

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。


示例 1：

输入：nums = [5,7,7,8,8, 8, 8,10], target = 8
输出：[3,4]
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        flag = False
        # 1. 搜索左边的, right + 1就是左边, right向左移动
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                flag = True
                right = mid - 1
        if not flag:
            return [-1, -1]
        res_left = right + 1
        # 2. 搜索右边的 left - 1就是右边的， left向右移动
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        res_right = left - 1
        return [res_left, res_right]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    s = Solution()
    res = s.searchRange(nums, target)
    print(res)
