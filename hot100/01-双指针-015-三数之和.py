"""
@Author: yanzx
@Date: 2022/3/21 0:07
@Description: 三数之和.py


给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
7
[0, 0, 1, 1, 1, 1, 2, 3, 4, 5, 6]

"""

from typing import List, Dict


#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [0, 0, 1, 1, 1, 1, 2, 3, 4, 5, 6]
        res = []

        # 排序
        nums.sort()
        length = len(nums)
        s = set()
        # 固定一个数字，作为第一个数字，然后找到另外两个数
        for i in range(length):
            # 保证第一个数字是唯一的
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 第一个数字 > 0，那么另外两个数字一定大于零
            elif nums[i] > 0:
                return res
            left, right = i + 1, length - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    # 官方给的：
                    # 去重，确定另一个数，那么第三数字一定确定
                    # 保证每一趟第二个数字是唯一的
                    tmp = [nums[i], nums[left], nums[right]]
                    res.append(tmp)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 保证每一趟第三个数字是唯一的
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

    def threeSum_2nd(self, nums: List[int]) -> List[List[int]]:
        """
        其实就是两个去重
        1. num去重
        2. left和right去重
        """
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # 去重
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 0, 0, 0, 2, 2]
    nums.sort()
    print(nums)
    res = s.threeSum(nums)
    print(res)
