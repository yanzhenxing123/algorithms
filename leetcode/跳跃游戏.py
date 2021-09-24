"""
@Author: yanzx
@Date: 2020/12/29 18:10
@Description: 
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        length = len(nums)
        flag = True
        for i in range(length-1, -1, -1):
            if nums[i] == 0 and flag and i != length-1:
                flag = False
                zero_index = i

            if not flag:
                if zero_index - i < nums[i]:
                    flag = True

        return flag

if __name__ == '__main__':
    s = Solution()
    nums = [0]
    res = s.canJump(nums)
    print(res)
