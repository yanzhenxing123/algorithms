"""
@Author: yanzx
@Date: 2025/3/19 16:30
@Description:
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        word1 = " " + word1
        word2 = " " + word2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j] + 1,
                    )
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    word1 = "intention"
    word2 = "execution"
    res = s.minDistance(word1, word2)
    print(res)
