"""
@Time: 2024/4/17 18:08
@Author: yanzx
@Desc: 最简单的dfs，也是最经典的模板
就是
def dfs(nums, path):
    if ...:
        return
    for _ in ...：
        path.append()
        dfs
        path.pop()

         1                  2             3
    1    2      3       1  2  3        1  2  3
 1 2 3  1 2 3 1 2 3 1 2 3 ....
"""
import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums: List[int], index: int, path: List[int]):
        if len(nums) == len(path):
            self.res.append(path.copy())
            return

        for i in range(index, len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.dfs(nums, 0, path)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    res = s.permute(nums)
    print(res)
