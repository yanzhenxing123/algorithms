"""
@Author: yanzx
@Date: 2021-10-04 14:01:58
@Desc:
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
"""

from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        z = 0
        for num in nums:
            z ^= num

        # 找到z的为1的最低位

        m = 1
        while z & m == 0:
            m <<= 1

        x, y = 0, 0
        for num in nums:
            if num & m == 0:
                x ^= num
            else:
                y ^= num
        return [x, y]


if __name__ == '__main__':
    pass
