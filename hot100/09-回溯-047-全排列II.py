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

import copy


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        其实可以暴力解决
        :param nums:
        :return:
        """
        res = []
        path_bools = [False] * len(nums)
        s = set()

        def dfs(nums, index, path, d_path):
            """
                         1                              1                          2
            -           1           2           1       1      2          1     1     2
        -            -  -  2       -  1  -      2
            """
            if len(path) == len(nums):
                tmp_str = "-".join(list(map(str, path)))
                if tmp_str in s:
                    return
                s.add(tmp_str)
                res.append(path.copy())
                return

            for i in range(0, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(nums, 0, path, d_path)
                path.pop()

        if not nums:
            return []
        nums.sort()
        dfs(nums, 0, [], {})
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        path_bools = [False] * len(nums)

        def dfs(nums, index, path, d_path):
            """
                         1                      1                       2
            1           1           2       1       1      2          1     1     2
        1  1  2      1  1  2       1  1  2
            """
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(0, len(nums)):

                if path_bools[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not path_bools[i - 1]:
                    print(path)
                    continue
                path.append(nums[i])
                path_bools[i] = True
                dfs(nums, 0, path, d_path)
                path_bools[i] = False
                path.pop()

        if not nums:
            return []
        nums.sort()
        dfs(nums, 0, [], {})
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    res = s.permuteUnique(nums)
    print(res)
