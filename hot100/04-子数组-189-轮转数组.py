"""
@Time: 2024/3/26 23:02
@Author: yanzx
@Desc:
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。



示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        length = len(nums)
        end_arr = nums[length - k:length]
        other_length = length - k
        for i in range(other_length - 1, -1, -1):
            nums[i + k] = nums[i]
        for j in range(len(end_arr)):
            nums[j] = end_arr[j]

    def rotate_2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        front_arr = nums[:n - k]
        end_arr = nums[n - k:]

        nums[:k] = end_arr
        nums[k:] = front_arr

    def rotate_no_space(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        # 1. 整体翻转
        i, j = 0, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        print(nums)
        # 2. 前边翻转
        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        print(nums)
        # 3. 后边翻转
        i, j = k, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        print(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    res = s.rotate_no_space(nums, k)
    print(nums)
