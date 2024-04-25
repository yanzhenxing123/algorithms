"""
@Time: 2024/4/24 23:24
@Author: yanzx
@Desc: left就是最终位置
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return left


if __name__ == '__main__':
    s = Solution()
    res = s.searchInsert(nums=[1, 3], target=2)
    print(res)
