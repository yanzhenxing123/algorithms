"""
@Time: 2024/8/22 14:25
@Author: yanzx
@Desc:
给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        1. dp[i] 表示这个数字拆分后乘积的最大值
        2.
        :param n:
        :return:
        """
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i // 2):
                dp[i] = max(j*(i - j), j * dp[i-j], dp[i])
        print(dp)
        return dp[n]



if __name__ == '__main__':
    s = Solution()
    res = s.integerBreak(3)
    print(res)
