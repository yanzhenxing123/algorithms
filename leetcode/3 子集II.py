"""
@Author: yanzx
@Date: 2020/12/6 22:29
@Description: 回溯
"""
import copy
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        path = []
        self.backtrack(nums, path)
        return self.res

    def backtrack(self, nums: List[int], path: List[int]):
        if sorted(path) not in self.res:
            self.res.append(sorted(path))

        # if len(path) == len(nums):
        #     return

        for i in range(len(nums)):
            path.append(nums[i])
            self.backtrack(nums[i + 1:], path)
            path.pop()


class Solution(object):
    def subsetsWithDup(self, nums):
        res, path = [], []
        nums.sort()
        self.dfs(nums, 0, res, path)
        return res

    def dfs(self, nums, index, res, path):
        res.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, res, path)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    res = s.subsets(nums=[4, 4, 4, 1, 4])
    print(res)
