"""
@Time: 2024/8/24 15:08
@Author: yanzx
@Desc: 
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        1. dp[i] 代表n = i时有多少种不同的BST情况
        2. dp[i] = dp[0]dp[i-1] + dp[1]dp[i-2] + ... + dp[i-1]dp[0]
        3. 初始化长度：n+1，且dp[0]=dp[1]=1
        :param n:
        :return:
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] = dp[j] * dp[i - 1 - j] + dp[i]

        print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.numTrees(10)
