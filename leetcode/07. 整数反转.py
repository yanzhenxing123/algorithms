"""
@Author: yanzx
@Date: 2021-07-28 13:44:38
@Desc:
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
"""


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x == 0:
            return 0
        elif x < 0:
            x_str = str(-x)
            res = "".join(reversed(x_str))
            res = -int(res)
        elif x > 0:
            x_str = str(x)
            res = "".join(reversed(x_str))
            res = int(res)
        print(res)

        if res < (-1 << 31) or res > (1 << 31) - 1:
            return 0
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.reverse(1463847412)
    print(res)