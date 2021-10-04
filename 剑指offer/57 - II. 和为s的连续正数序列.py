"""
@Author: yanzx
@Date: 2021-10-04 14:56:48
@Desc:输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

输入：target = 9
输出：[[2,3,4],[4,5]]

解决方法：滑动窗口
"""

from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right, s = 1, 2, 3
        res = []
        while left < right:
            if s == target:
                res.append(list(range(left, right + 1)))
            if s >= target:
                s -= left
                left += 1
            else:
                right += 1
                s += right
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.findContinuousSequence(9)
    print(res)
