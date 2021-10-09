"""
@Author: yanzx
@Date: 2021-10-09 20:03:03
@Desc:

从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，
即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

大小王就是一个赖子

"""

from typing import List
from collections import Counter


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        # 有大小王
        if 0 in counter:
            counter.pop(0)
        for value in counter.values():
            if value > 1:
                return False
        max_num, min_num = max(counter), min(counter)
        return max_num - min_num <= 4


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 0, 4, 0]
    res = s.isStraight(nums)
    print(res)
