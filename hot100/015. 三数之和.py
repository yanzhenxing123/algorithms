"""
@Time: 2024/3/24 14:55
@Author: yanzx
@Desc:

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。


输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # 去重
                continue
            cur_num = nums[i]
            left, right = i + 1, len(nums) - 1  # 为什么从i，因为前面的已经完全考虑过了
            while left < right:
                if nums[left] + nums[right] > -cur_num:
                    right -= 1
                elif nums[left] + nums[right] < -cur_num:
                    left += 1
                else:
                    # 要考虑去重
                    tripe = [cur_num, nums[left], nums[right]]
                    res.append(tripe)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = s.threeSum(nums)
    print(res)
