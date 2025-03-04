"""
@Time: 2024/8/21 17:34
@Author: yanzx
@Desc:

给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。




示例 1：

输入：n = 12
输出：3
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9

dp[i]表示: 最少需要多少个数的平方来表示整数i

n = 13

1 = 1
2 = 1 + 1
3 = 1 + 1 + 1
4 = 2^2
5 = 2^2 + 1
6 = 2^2 + 1 + 1
7 = 2^2 + 1 + 1 + 1
8 = 2^2 + 2^2
9 = 3^2
10 = 3^2 + 1
11 = 3^2 + 1 + 1
12 = 2^2 + 2^2 + 2^2

[0, 1, 2, 3, 1, 2, ]


"""


class Solution:
    def numSquares(self, n: int) -> int:
        """
        dp[i]：表示当前最小平方数之和的个数
        dp[k] = dp[k - j * j] + 1
        j * j <= k
        :param n:
        :return:
        """
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            j = 1
            minn = float("inf")
            while j * j <= i:
                minn = min(dp[i - j * j], minn)
                j += 1
            dp[i] = minn + 1
            print(i, dp)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    res = s.numSquares(12)
    print(res)
