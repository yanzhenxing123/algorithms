"""
@Time: 2024/8/16 18:25
@Author: yanzx
@Desc: 感觉这个电脑
"""

from typing import List
import random
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        最优解
        也是快排的思想，random进行选择递归
        时间复杂度为O(n)
        """
        pivot = random.choice(nums)
        la, eq, sm = [], [], []  # 大、等、小
        for num in nums:
            if num > pivot:
                la.append(num)  # 比pivot大的
            elif num == pivot:
                eq.append(num)
            else:
                sm.append(num)  # 比pivot小的

        if len(la) < k <= len(la) + len(eq):  # 递归终止条件
            return pivot
        if len(la) >= k:  # 目标元素在la中
            return self.findKthLargest(la, k)
        else:  # 目标元素sm中，不可能在eq中
            return self.findKthLargest(sm, k - len(la) - len(eq))  # 减去 la和eq中的个数

    def findKthLargest_3rd(self, nums: List[int], k: int) -> int:
        la, eq, sm = [], [], []
        pivot = random.choice(nums)
        for num in nums:
            if num > pivot:
                la.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                sm.append(num)

        if len(la) < k <= len(eq) + len(la):
            return pivot
        elif len(la) >= k:
            return self.findKthLargest_3rd(la, k)
        else:
            return self.findKthLargest_3rd(sm, k - len(eq) - len(la))

    def findKthLargest_2nd(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        la = []
        eq = []
        sm = []

        for num in nums:
            if num > pivot:
                la.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                sm.append(num)

        if len(la) < k <= len(la) + len(eq):
            return pivot
        if len(la) >= k:
            return self.findKthLargest_2nd(la, k)
        else:
            return self.findKthLargest(sm, k - len(la) - len(eq))

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        使用快排的思想，通过不了, 超出时间限制
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

        def topk_split(nums, left, right, K):
            """
            直到第k个左边都小，右边都大
            :param nums:
            :param left:
            :param right:
            :param k:
            :return:
            """

            while left <= right:
                pivot_index = partition(nums, left, right)
                if pivot_index == K:
                    return pivot_index
                if pivot_index < K:  # K在右边
                    left = pivot_index + 1
                else:
                    right = pivot_index - 1

        def topk_split_recursive(nums, left, right, K):
            if left > right:
                return -1
            pivot_index = partition(nums, left, right)
            if pivot_index == K:
                return pivot_index
            elif pivot_index < K:
                return topk_split_recursive(nums, pivot_index + 1, right, K)
            else:
                return topk_split_recursive(nums, left, pivot_index - 1, K)

        left = 0
        right = len(nums) - 1
        K = len(nums) - k
        topk_split(nums, left, right, K)
        res = nums[K]
        return res

    def findKthLargest_by_heap(self, nums: List[int], k: int) -> int:
        # 先将前k个元素入堆
        heap = [nums[i] for i in range(0, k)]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)  # 弹出堆顶元素
                heapq.heappush(heap, nums[i])  # nums[i] 入堆
        return heap[0]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    s.findKthLargest(nums, 2)
