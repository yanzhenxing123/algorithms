"""
@Author: yanzx
@Date: 2021-08-17 10:40:01
@Desc: 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""

from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] % 2 == 0:
        #         nums.append(nums[i])
        #         nums.pop(i)
        # return nums

        # 左边奇数 右边偶数 双指针
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] % 2 == 0:
                if nums[right] % 2 == 1:
                    nums[left], nums[right] = nums[right], nums[left]
                else:
                    right -= 1
            else:
                left += 1
        return nums



if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    res = s.exchange(nums)
    print(res)
