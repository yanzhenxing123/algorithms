"""
@Time: 2025/3/24 17:05
@Author: yanzx
@Desc: 
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        fast = slow = 0

        n = len(nums)
        while fast < n:
            pass


if __name__ == '__main__':
    s = Solution()
    nums = [5, 1, 1, 2, 0, 0]
    res = s.sortArray(nums)
    print(res)
