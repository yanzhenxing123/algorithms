"""
@Author: yanzx
@Date: 2020/12/29 17:18
@Description: 
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        length = len(nums)
        res = [0] * (length + 1)
        res[1] = nums[0]
        for i in range(2, length+1):
            res[i] = max(res[i-1], nums[i-1]+res[i-2])
        print(res)
        return res[-1]

if __name__ == '__main__':
    s = Solution()
    nums = [1,2]
    res = s.rob(nums)
    print(res)
