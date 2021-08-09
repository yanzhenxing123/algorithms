"""
@Author: yanzx
@Date: 2021/8/4 22:13
@Description:
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

0 1 2 3 4 5 6 7 8
0 0 1 2 4 6 9 12

                                      都不剪  左剪右剪     左剪右边不剪
动态规划 dp[i] = max(dp[i], max(j * (i-j), dp[j]*dp[i-j], dp[j]*(i-j))
"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        # 动态规划问题
        if n == 0 or n == 1:
            return 0
        dp = [0 for _ in range(1 + n)]
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(j*(i-j), j*dp[i-j], dp[j]*dp[i-j], dp[i])
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    res = s.cuttingRope(10)
    print(res)



