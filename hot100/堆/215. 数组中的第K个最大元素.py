"""
@Time: 2024/8/16 18:25
@Author: yanzx
@Desc: 
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(nums, left, right):
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]

            nums[left] = pivot
            return left

        def topk_split(nums, left, right, k):
            """
            直到第k个左边都小，右边都大
            :param nums:
            :param left:
            :param right:
            :param k:
            :return:
            """
            if left <= right:
                index = partition(nums, left, right)
                if index == k:
                    return
                if index < k:
                    topk_split(nums, index + 1, right, k)
                else:
                    topk_split(nums, left, index - 1, k)
        left = 0
        right = len(nums) - 1
        topk_split(nums, left, right, len(nums) - k)
        res = nums[len(nums) - k]
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [5]
    s.findKthLargest(nums, 1)
