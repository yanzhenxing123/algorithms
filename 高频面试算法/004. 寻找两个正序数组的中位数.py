"""
@Author: yanzx
@Date: 2021-12-01 18:51:40
@Desc:

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。


算法的时间复杂度应该为 O(log (m+n))

"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        index = length // 2
        if length % 2 == 1:
            return nums1[index]
        return (nums1[index - 1] + nums1[index]) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) / 2


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2, 3]
    res = s.findMedianSortedArrays(nums1, nums2)
    print(res)
