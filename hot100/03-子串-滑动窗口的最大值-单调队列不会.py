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
from collections import deque
import collections

from collections import deque


class MyQueue:  # 单调队列（从大到小
    def __init__(self):
        self.queue = deque()  # 这里需要使用deque实现单调队列，直接使用list会超时

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    # 同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()  # list.pop()时间复杂度为O(n),这里需要使用collections.deque()

    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    # 这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    # 查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k):  # 先将前k的元素放进队列
            que.push(nums[i])
        result.append(que.front())  # result 记录前k的元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i - k])  # 滑动窗口移除最前面元素
            que.push(nums[i])  # 滑动窗口前加入最后面的元素
            result.append(que.front())  # 记录对应的最大值
        return result


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        最优解 代码最少
        :param nums:
        :param k:
        :return:
        """
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res


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
