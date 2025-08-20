"""
@Author: yanzx
@Date: 2025/3/19 16:30
@Description:

init:
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]




[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
 [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10],
 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
 [1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10],
 [2, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9],
 [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



word1 = "horse"
word2 = "ros"

# 初始化dp数组
dp = [
    [0, 1, 2, 3],  # 空字符串到word2的编辑距离
    [1, ?, ?, ?],   # "h"到word2的编辑距离
    [2, ?, ?, ?],   # "ho"到word2的编辑距离
    [3, ?, ?, ?],   # "hor"到word2的编辑距离
    [4, ?, ?, ?],   # "hors"到word2的编辑距离
    [5, ?, ?, ?]    # "horse"到word2的编辑距离
]


# 填充过程
# dp[1][1]: "h" → "r" = 1 (替换)
# dp[1][2]: "h" → "ro" = 2 (插入o)
# dp[1][3]: "h" → "ros" = 3 (插入o和s)

# dp[2][1]: "ho" → "r" = 2 (删除o)
# dp[2][2]: "ho" → "ro" = 1 (插入o)
# dp[2][3]: "ho" → "ros" = 2 (插入s)

# 最终结果：dp[5][3] = 3
# "horse" → "ros" 需要3步：
# 1. horse → rorse (删除h)
# 2. rorse → rose (删除r)
# 3. rose → ros (删除e)

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        print(dp)
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
            print(dp)
        return dp[-1][-1]

    def minDistance_2nd(self, word1: str, word2: str) -> int:
        """
        二刷
        :param word1:
        :param word2:
        :return:
        """
        m, n = len(word1), len(word2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        # 初始化dp
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        word1 = " " + word1
        word2 = " " + word2
        for i in range(1, m+1):
            for j in range(1, n +1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[-1][-1]







if __name__ == '__main__':
    s = Solution()
    word1 = "intention"
    word2 = "executionaa"
    res = s.minDistance_2nd(word1, word2)
    print(res)
