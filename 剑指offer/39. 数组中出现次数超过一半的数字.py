"""
@Author: yanzx
@Date: 2021-09-25 00:07:24
@Desc: 数组中出现次数超过一半的数字

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

遍历数组，若后面那一个等于前面那一个，count+=1
         若后面那一个不等于前面那一个，count-=1
         count = 0时，重置count，重置res

"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        res = nums[0]
        for num in nums:
            if num == res:
                count += 1
            else:
                count -= 1
            if count == 0:
                res = num
                count += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    res = s.majorityElement(nums)
    print(res)