"""
@Time: 2024/4/21 16:43
@Author: yanzx
@Desc: 
"""

from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums: List[int], index: int, path: List[int]):
        pass




if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 6, 7]
    target = 7
    res = s.combinationSum(nums, target)
    print(res)
