"""
@Time: 2024/4/18 10:23
@Author: yanzx
@Desc:



        1              2         3
     2   3             3
   3




示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums: List[int], index: int, path: List[int]):
        self.res.append(path.copy())
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    res = s.subsets(nums)
    print(res)
