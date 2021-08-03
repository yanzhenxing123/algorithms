"""
@Author: yanzx
@Date: 2021/8/3 0:10
@Description: 
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # 找到旋转点也就是最小值
        while left < right:
            mid = left + (right - left) // 2
            if nums[right] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                right -= 1
        mid = left
        left, right = 0, len(nums) - 1
        if nums[mid] == target:
            return mid
        if nums[right] >= target:
            return self.binary_search(nums, mid + 1, right, target)
        else:
            return self.binary_search(nums, left, mid - 1, target)

    def binary_search(self, arr, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    nums = [1, 3]
    target = 3
    s = Solution()
    res = s.search(nums, target)
    print(res)
