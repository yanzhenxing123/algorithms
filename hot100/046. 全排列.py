"""
@Time: 2024/4/17 18:08
@Author: yanzx
@Desc: 最简单的dfs
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
        res = []

        def dfs(nums: List[int], path: List[int]):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                dfs(nums, path)
                path.pop()

        dfs(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    res = s.permute(nums)
    print(res)
