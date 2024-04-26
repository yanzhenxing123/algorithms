"""
@Time: 2024/4/26 22:32
@Author: yanzx
@Desc:
旋转数组中寻找target的前半部分

输入：nums = [3,4,5,1,2]
输出：1
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_index = -1
        while left <= right:
            # 如果有序，left就是min_index
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid] <= nums[right]:
                min_index = left
                break
            if nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[right] > nums[mid]:
                right = mid
        return nums[min_index]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    res = s.findMin(nums)
    print(res)
