"""
@Time: 2024/4/18 10:23
@Author: yanzx
@Desc:



给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的
子集
（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。




           1                2               2                3
     2     2    3       2       3           3
   2  3    3          3
 3

示例 1：

输入：nums = [1,2,2,3]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

"""

from typing import List
import copy


class Solution(object):
    def subsetsWithDup(self, nums):
        res, path = [], []
        nums.sort()
        self.dfs(nums, 0, res, path)
        return res

    def dfs(self, nums, index, res, path):
        """
        考虑如何剪枝，if i > index and nums[i] == nums[i-1]就不用递归了
        :param nums:
        :param index:
        :param res:
        :param path:
        :return:
        """
        res.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, res, path)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2, 3]
    res = s.subsetsWithDup(nums)
    print(res)
