"""
@Author: yanzx
@Date: 2020/10/27 17:10
@Description: 
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
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    s = Solution()
    res = s.maxSlidingWindow(nums, k)
    print(res)

