"""
@Author: yanzx
@Date: 2021-11-24 21:29:19
@Desc: 数组中的第K个最大元素


"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快排，然后找到最大的
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums[-k]

    def quick_sort(self, arr, left, right):
        if left < right:
            mid = self.partition(arr, left, right)
            self.quick_sort(arr, left, mid - 1)
            self.quick_sort(arr, mid + 1, right)

    def partition(self, arr, left, right):
        pivot = arr[left]

        while left < right:
            # 停止条件left == right
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]

        arr[right] = pivot

        return right


if __name__ == '__main__':
    s = Solution()
    res = s.findKthLargest([1, 2, 3, 1], 1)
    print(res)
