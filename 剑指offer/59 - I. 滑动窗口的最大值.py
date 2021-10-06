"""
@Author: yanzx
@Date: 2021-10-06 16:32:40
@Desc: 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。


输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]

解题思路：维护一个双端队列，队列中的值为nums中的索引，头最大，尾最小
"""

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        length = len(nums)
        # k不满足的终止条件
        if k < 2 or length < 2:
            return nums
        # 初始化队列结果和队列
        res, queue = [], []
        for i in range(length):
            # 双端队列 头最大 尾最小
            if len(queue) == 0:
                queue.append(i)
            # 比头大
            elif nums[i] > nums[queue[0]]:
                queue.clear()
                queue.append(i)

            # 比尾小
            elif nums[i] <= nums[queue[-1]]:
                queue.append(i)
            # 比头小 比尾大
            else:
                while nums[i] > nums[queue[-1]]:
                    queue.pop(-1)
                queue.append(i)
            # 滑动窗口为k之后才能添加到结果中
            if i >= k-1:
                res.append(nums[queue[0]])
            # 队列修剪
            if i - queue[0] >= k - 1:
                queue.pop(0)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    res = s.maxSlidingWindow(nums, k)
    print(res)
