"""
@Author: yanzx
@Date: 2025/12/01 16:00
@Description:
虾皮一面算法题

dp[i][j]：text[0:i] 和 text[0:j] 最大的公共子序列


"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m = len(text1)
        n = len(text2)
        dp = [
            [0 for _ in range((n + 1))] for _ in range(m + 1)
        ]

        text1 = " " + text1
        text2 = " " + text2
        for i in range(1, m + 1):
            char1 = text1[i]
            for j in range(1, n + 1):
                char2 = text2[j]
                if char1 == char2:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    text1 = "abcde"
    text2 = "ace"
    res = s.longestCommonSubsequence(text1, text2)
    print(res)
