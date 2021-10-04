"""
@Author: yanzx
@Date: 2021-09-28 07:59:53
@Desc: 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
输入: [7,5,6,4]
输出: 5

"""

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums))]
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            print(i)
            j = i+1
            while j < len(nums):
                if nums[i] > nums[j]:
                    dp[i] = dp[j] + 1
                    break
                elif nums[i] == nums[j]:
                    dp[i] = dp[j]
                    break
                else:
                    j = j + 1

        print(dp)
        return sum(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [7, 5, 6, 4]
    res = s.reversePairs(nums)
    print(res)
