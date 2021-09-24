"""
@Author: yanzx
@Date: 2020/12/19 20:33
@Description:
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]
输出: 3
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_num = max(nums)
        if min_num < 0:
            return 1
        for num in nums:
            if num > 0 and num < min_num:
                min_num = num
        if min_num == 1:
            for i in range(0, max(nums)-min_num+1):
                min_num += 1
                if min_num not in nums:
                    return min_num

        return 1






if __name__ == '__main__':
    s = Solution()
    res = s.firstMissingPositive([1,2,0])
    print(res)

