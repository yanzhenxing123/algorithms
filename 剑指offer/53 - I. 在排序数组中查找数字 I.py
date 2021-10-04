"""
@Author: yanzx
@Date: 2021-10-04 19:18:01
@Desc:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

统计一个数字在排序数组中出现的次数。


"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = self.binary_search(nums, target)
        res = 0
        if mid is None:
            return res
        for i in range(mid, len(nums)):
            if nums[i] == target:
                res += 1
        for i in range(mid-1, -1, -1):
            if nums[i] == target:
                res += 1

        return res

    def binary_search(self, nums: List[int], target: int):
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
        return None

class Solution2:
    def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                # 找到右边界
                if nums[m] <= tar:
                    i = m + 1
                else: j = m - 1
            print(i)
            return i
        return helper(target) - helper(target - 1)

if __name__ == '__main__':
    nums = [5, 8, 8, 10]
    target = 8
    s = Solution2()
    res = s.search(nums, target)
