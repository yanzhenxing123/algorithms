"""
@Author: yanzx
@Date: 2021-10-04 19:50:24
@Desc:
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    res = s.missingNumber(nums)
    print(res)
