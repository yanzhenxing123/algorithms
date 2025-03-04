"""
@Time: 2024/8/16 18:25
@Author: yanzx
@Desc: 
"""

from typing import List
import random
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        也是快排的思想，random进行选择递归
        时间复杂度为O(n)
        """
        pivot = random.choice(nums)
        la, eq, sm = [], [], []  # 大、等、中
        for num in nums:
            if num > pivot:
                la.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                sm.append(num)

        if len(la) < k <= len(la) + len(eq):  # 递归终止条件
            return pivot
        if len(la) >= k:  # 目标元素在左边
            return self.findKthLargest(la, k)
        else:  # 目标元素在右边
            return self.findKthLargest(sm, k - len(la) - len(eq))  # 减去 la和eq中的个数

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        """
        使用堆, 容量为k的小跟堆存储最大的元素，堆顶元素就是要的结果
        :param nums:
        :param k:
        :return:
        """
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if num > min_heap[0]:
                    heapq.heapreplace(min_heap, num)
        return min_heap[0]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        使用快排的思想
        :param nums:
        :param k:
        :return:
        """

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
                if index < k:  # 右边
                    topk_split(nums, index + 1, right, k)
                else:  # 左边
                    topk_split(nums, left, index - 1, k)

        left = 0
        right = len(nums) - 1
        topk_split(nums, left, right, len(nums) - k)
        res = nums[len(nums) - k]
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    s.findKthLargest(nums, 2)
