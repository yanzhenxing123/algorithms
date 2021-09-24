"""
@Author: yanzx
@Date: 2021/4/20 10:42
@Description:
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
"""
import sys  # 导入sys模块
sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000


from typing import List


class Solution:
    # 回溯 + 剪枝
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        self.back_track(candidates, [], target)
        return self.res

    def back_track(self, candidates, path, target):
        if sorted(path) not in self.res and sum(path) == target:
            self.res.append(sorted(path))
            return

        if sum(path) > target:
            return

        for candidate in candidates:
            path.append(candidate)
            self.back_track(candidates, path, target)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    candidates = [2,3,5]
    res = s.combinationSum(candidates, target=8)
    print(res)
