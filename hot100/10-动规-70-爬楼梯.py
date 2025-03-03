"""
@Author: yanzx
@Date: 2025/3/3 20:57
@Description:
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a1 = 1
        a2 = 2
        a3 = a1 + a2
        for i in range(2, n):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
        return a3


if __name__ == '__main__':
    s = Solution()
