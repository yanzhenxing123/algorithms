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

    def findKthLargest_2nd(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        lagers = []
        equals = []
        smallers = []
        for num in nums:
            if num > pivot:
                lagers.append(num)
            elif num == pivot:
                equals.append(num)
            else:
                smallers.append(num)

        if len(lagers) < k <= len(lagers) + len(equals):
            return pivot
        if len(lagers) >= k:
            return self.findKthLargest_2nd(lagers, k)
        else:
            return self.findKthLargest_2nd(smallers, k - len(lagers) - len(equals))

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

        left = 0
        right = len(nums) - 1
        K = len(nums) - k
        topk_split(nums, left, right, K)
        res = nums[K]
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    s.findKthLargest(nums, 2)
