"""
@Time: 2024/4/26 22:44
@Author: yanzx
@Desc: 
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        if len(a) > len(b):
            a, b = b, a  # 保证下面的 i 可以从 0 开始枚举, 保证a的长度短

        m, n = len(a), len(b)
        a = [float('-inf')] + a + [float('inf')]
        b = [float('-inf')] + b + [float('inf')]

        # 枚举 nums1 有 i 个数在第一组
        # 那么 nums2 有 j = (m + n + 1) // 2 - i 个数在第一组
        i, j = 0, (m + n + 1) // 2
        while True:
            if a[i] <= b[j + 1] and a[i + 1] > b[j]:  # 写 >= 也可以
                max1 = max(a[i], b[j])  # 第一组的最大值
                min2 = min(a[i + 1], b[j + 1])  # 第二组的最小值
                if (m + n) % 2:
                    return max1
                else:
                    return (max1 + min2) / 2
            i += 1  # 继续枚举
            j -= 1


class Solution_2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2

        return (self.findKth(nums1, 0, nums2, 0, left) + self.findKth(nums1, 0, nums2, 0, right)) / 2.0

    def findKth(self, nums1: List[int], i: int, nums2: List[int], j: int, k: int) -> int:
        # i: nums1的起始位置, j: nums2的起始位置
        if i >= len(nums1):
            return nums2[j + k - 1]  # nums1为空数组
        if j >= len(nums2):
            return nums1[i + k - 1]  # nums2为空数组
        if k == 1:
            return min(nums1[i], nums2[j])

        # 获取两个数组的第k//2个元素
        mid_val1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else float('inf')
        mid_val2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) else float('inf')

        if mid_val1 < mid_val2:
            return self.findKth(nums1, i + k // 2, nums2, j, k - k // 2)
        else:
            return self.findKth(nums1, i, nums2, j + k // 2, k - k // 2)


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    res = s.findMedianSortedArrays(nums1, nums2)
    print(res)
