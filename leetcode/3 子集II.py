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
            self.backtrack(nums[i+1:], path)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    res = s.subsets(nums=[4,4,4,1,4])
    print(res)
