"""
@Author: yanzx
@Date: 2021-08-03 13:51:46
@Desc: 全排列
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs_helper(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(0, len(nums)):
                # 去除重复值
                if nums[i] in set(path):
                    continue
                path.append(nums[i])
                dfs_helper(path)
                path.pop()

        dfs_helper([])
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.permute([1, 2, 3])
    print(res)
