"""
@Time: 2024/4/21 16:21
@Author: yanzx
@Desc:
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。


输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。


                                             2                                      3       6        7
                            2            3       6        7
                        2  3  6  7
                2  3  6  7
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.res

    def dfs(self, candidates: List[int], target: int, index: int, path: List[int]):
        print(path)
        if sum(path) == target:
            self.res.append(path.copy())
            return
        for i in range(index, len(candidates)):  # 横着走
            path.append(candidates[i])
            if sum(path) > target:  # 说明这一行就不行了
                path.pop()
                break
            self.dfs(candidates, target, i, path)  # 往下
            path.pop()


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    res = s.combinationSum(candidates, target)
    print(res)
