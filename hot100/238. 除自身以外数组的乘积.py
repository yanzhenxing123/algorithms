"""
@Time: 2024/3/27 10:37
@Author: yanzx
@Desc:

给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。
请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        不能使用除法, 算出来左边元素和右边元素的乘积
        :param nums:
        :return:
        """
        length = len(nums)
        left_arr = [0] * length
        right_arr = [0] * length
        res = [0] * length
        for i in range(0, length):
            if i == 0:
                left_arr[i] = 1
            else:
                left_arr[i] = left_arr[i - 1] * nums[i - 1]
        for j in range(length - 1, -1, -1):
            if j == length - 1:
                right_arr[j] = 1
            else:
                right_arr[j] = right_arr[j + 1] * nums[j + 1]
        for k in range(len(nums)):
            res[k] = left_arr[k] * right_arr[k]
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    res = s.productExceptSelf(nums)
    print(res)
