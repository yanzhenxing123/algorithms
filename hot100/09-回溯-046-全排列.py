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


           1               2                  3
     -    2      3    1      3
          3      2


"""
import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.flags = [False] * len(nums)
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums: List[int], index: int, path: List[int]):
        if len(nums) == len(path):
            self.res.append(path.copy())
            return

        for i in range(index, len(nums)):
            if self.flags[i]:
                continue
            path.append(nums[i])
            self.flags[i] = True
            self.dfs(nums, 0, path)
            self.flags[i] = False
            path.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    res = s.permute(nums)
    print(res)
