"""
@Author: yanzx
@Date: 2021/4/20 11:16
@Description: 不包括重复的
"""

from typing import List


class Solution:
    # 回溯 + 剪枝
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def back_track(path: List, index: int, sum_now: int):
            if sum_now == target:
                res.append(path[:])
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                sum_now += candidates[i]
                if sum_now > target:
                    sum_now -= candidates[i]
                    return
                path.append(candidates[i])
                back_track(path, i+1, sum_now)
                path.pop()
                sum_now -= candidates[i]

        back_track([], 0, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    candidates = [10,1,2,7,6,1,5]
    res = s.combinationSum(candidates, target=8)
    print(res)
