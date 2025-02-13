"""
@Time: 2024/8/9 11:21
@Author: yanzx
@Desc:

找到转折点，也就是最小值的点

示例 1：

输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

条件：每个元素值互不相同
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        重点是如何找到最小值的index
        1. nums[left] <= nums[mid] <= nums[right] 返回 left
        2. mid在左半部分, left = mid + 1
        3. mid在右半部分，且left在左半部分, right = mid
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        min_index = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] <= nums[right]:  # 逼近最小的点
                min_index = left
                break
            if nums[left] <= nums[mid]:
                left = mid + 1
            if nums[mid] <= nums[right]:
                right = mid
        return nums[min_index]


if __name__ == '__main__':
    s = Solution()
    # nums = [3, 4, 5, 1, 2]
    nums = [1, 2, 3, 4, 5]
    res = s.findMin(nums)
    print(res)
