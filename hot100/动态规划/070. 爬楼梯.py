"""
@Time: 2024/8/21 16:54
@Author: yanzx
@Desc: 
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        n0 = 1
        n1 = 1
        if n == 0 or n == 1:
            return 1
        for i in range(2, n + 1):
            res = n0 + n1
            n0 = n1
            n1 = res
            print(res)
        return res


if __name__ == '__main__':
    s = Solution()
    s.climbStairs(10)