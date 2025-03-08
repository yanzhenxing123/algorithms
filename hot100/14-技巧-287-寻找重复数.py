"""
@Author: yanzx
@Date: 2025/3/8 11:37
@Description:
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。



示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
示例 3 :

输入：nums = [3,3,3,3,3]
输出：3

类似于有环的链表

"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            # fast 前进两次，slow 前进一次
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast:
                break

        # ptr == slow 时说明检测到重复元素，两个重复元素同时指向环的入口。
        ptr = 0
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]

        return ptr



