"""
@Author: yanzx
@Date: 2021-10-06 15:16:48
@Desc: 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            n2 = dp[index2] * 2
            n3 = dp[index3] * 3
            n5 = dp[index5] * 5
            dp[i] = min(n2, n3, n5)
            if n2 == dp[i]:
                index2 += 1
            if n3 == dp[i]:
                index3 += 1
            if n5 == dp[i]:
                index5 += 1

        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    res = s.nthUglyNumber(10)
    print(res)
