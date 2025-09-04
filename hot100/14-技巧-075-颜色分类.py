"""
@Author: yanzx
@Date: 2025/3/8 11:17
@Description:
75. 颜色分类

给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:  # 这个地方必须是<=因为还需要和前面的进行比较
            while i <= p2 and nums[i] == 2:  # 这个地方一定是while因为保持最后面的数字都是2且nums[i] != 2
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1


if __name__ == '__main__':
    nums = [2, 0, 1]
    s = Solution()
    res = s.sortColors(nums)
    print(nums)
