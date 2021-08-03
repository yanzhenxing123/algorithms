"""
@Author: yanzx
@Date: 2021/8/2 21:24
@Description:

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1

        res = self.fib(n-1) + self.fib(n-2)
        return int(res % (1e9 + 7))

    def fib2(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        last, last2 = 1, 1
        res = None
        for i in range(2, n):
            res = last2 + last
            last = last2
            last2 = res
        return int(res % (10 ** 9 + 7))

if __name__ == '__main__':
    s = Solution()
    res = s.fib2(81)
    print(res)
