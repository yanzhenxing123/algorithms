"""
@Time: 2024/3/25 16:22
@Author: yanzx
@Desc:
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。 子数组是数组中元素的连续非空序列。
示例 1：
输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums =       [1, 2, 3], k = 3
输出：2
    pre_sum = [0, 1, 3, 6]

    1 3  6
      2  5
         3

思路：
1. 快慢指针 ❎
2. 前缀和 ✅
这题不熟练
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        暴力前缀和，注意添加个0
        :param nums:
        :param k:
        :return:
        """
        res = 0
        d = {0: 1}  # 合为0的子数组有几个
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            another = pre - k
            res += d.get(another, 0)
            d[pre] = d.get(pre, 0) + 1
        return res

    def subarraySum1(self, nums: List[int], k: int) -> int:
        """
        这个一定要写出来
        暴力前缀和，注意添加个0
        时间超出限制
        :param nums:
        :param k:
        :return:
        """
        res = 0
        if not nums:
            return 0
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(sum(nums[0:i + 1]))
        for i in range(0, len(pre_sum) - 1):
            for j in range(i + 1, len(pre_sum)):
                if pre_sum[j] - pre_sum[i] == k:
                    res += 1
        return res

    def subarraySum2(self, nums: List[int], k: int) -> int:
        """
        错误的
        :param nums:
        :param k:
        :return:
        """
        if not nums:
            return 0
        res = 0
        queue = []
        slow, fast = 0, 0
        queue.append(nums[slow])
        while fast < len(nums) and slow <= fast:
            print(queue)
            if sum(queue) == k:
                res += 1
                slow += 1
                queue.pop(0)
            elif sum(queue) < k and fast < len(nums) - 1:
                fast += 1
                queue.append(nums[fast])
            elif sum(queue) > k and slow < fast:
                slow += 1
                queue.pop(0)
            else:
                slow += 1
                fast += 1

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, -1, 0]
    k = 0
    res = s.subarraySum(nums, k)
    print(res)
