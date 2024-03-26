"""
@Time: 2024/3/26 11:08
@Author: yanzx
@Desc:

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。


示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

from typing import List
from  collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        使用单调队列，存的是一个从左到右递减的 存下标即可
        [3, -1]
        [3 -1, -3]
        [5]
        [5, 3]
        [6]
        [7]
        :param nums:
        :param k:
        :return:
        """
        q = deque()
        res = []
        for i in range(k):  # 初始化queue
            if not q:
                q.append(i)
            elif nums[q[-1]] >= nums[i]:
                q.append(i)
            else:
                while q and nums[q[-1]] < nums[i]:
                    q.pop()
                q.append(i)
        res.append(nums[q[0]])
        for i in range(k, len(nums)):
            # 1. 添加队尾
            if nums[q[-1]] >= nums[i]:
                q.append(i)
            else:
                while q and nums[q[-1]] < nums[i]:
                    q.pop()
                q.append(i)
            # 2. 去除对首
            if i - k == q[0]:
                q.popleft()
            res.append(nums[q[0]])
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """
        使用set进行 错误
        :param nums:
        :param k:
        :return:
        """
        if len(nums) <= k:
            return [max(nums)]

        res = []
        s = set()
        max_num = max(nums[:k])
        res.append(max_num)
        for i in range(k):
            if nums[i] == max_num:
                s.add(i)
        for i in range(1, len(nums) - k + 1):
            if nums[i + k - 1] > max_num:  # 大于清空
                max_num = nums[i + k - 1]
                s.clear()
                s.add(i + k - 1)
            else:
                if nums[i - 1] == max_num:
                    s.remove(i - 1)
                if nums[i + k - 1] == max_num:
                    s.add(i + k - 1)

                if not s:
                    max_num = nums[i]
                    s.add(i)
                    for j in range(1, k):
                        if nums[i + j] > max_num:
                            s.clear()
                            s.add(i + j)
                            max_num = nums[i + j]
                        elif nums[i + j] == max_num:
                            s.add(i + j)
            res.append(max_num)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 1, 2, 0, 5]

    k = 3
    res = s.maxSlidingWindow(nums, k)
    print(res)
