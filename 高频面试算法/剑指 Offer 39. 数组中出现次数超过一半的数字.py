"""
@Author: yanzx
@Date: 2021-12-01 18:08:32
@Desc:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2


摩尔投票

遍历一遍可以得到出现次数最多的数字

"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if count == 0:
                res = num
                count += 1
            else:
                if res == num:
                    count += 1
                else:
                    count -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [3, 3, 4]
    res = s.majorityElement(nums)
    print(res)
