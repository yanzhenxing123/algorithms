"""
@Author: yanzx
@Date: 2021-10-04 14:34:13
@Desc:
输入：[3,30,34,5,9]
输出: "3033459"
"""
import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(sort_rule))
        return "".join(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [3, 30, 4, 5, 9]
    res = s.minNumber(nums)
    print(res)
