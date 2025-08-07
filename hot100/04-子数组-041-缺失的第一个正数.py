"""
@Time: 2024/3/27 11:41
@Author: yanzx
@Desc:
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

示例 1：

输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。
示例 2：

输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。
示例 3：

输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。
"""

from typing import List

from collections import deque


class Solution:


    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        将位置变换
        将0 < nums[i] <= len(nums)的数字放到自己的位置上
        :param nums:
        :return:
        """

        if not nums:
            return 1
        nums = [0] + nums
        i = 1
        while i < len(nums):
            if 0 < nums[i] < len(nums) and nums[nums[i]] != nums[i]:  # 第一个条件，元素不超过长度 且 要放的位置上不是当前元素
                # 把当前元素放到要放的位置
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
            else:  # 第二个条件
                i += 1
                continue
        # 返回结果
        for i in range(1, len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    def firstMissingPositive_2nd(self, nums: List[int]) -> int:
        """
        2nd solution
        :param nums:
        :return:
        """
        for i in range(len(nums))
        pass


if __name__ == '__main__':
    s = Solution()
    nums = [2]
    res = s.firstMissingPositive(nums=nums)
    print(res)
