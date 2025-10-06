"""
@Author: yanzx
@Time: 2025/8/25 01:17 
@Description:

在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

输入：matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
输出：4
示例 2：


输入：matrix = [["0","1"],
             ["1","0"]]
输出：1
示例 3：

输入：matrix = [["0"]]
输出：0

正方形：
0 1 1 1 0
1 1 1 1 0
0 1 1 1 1
0 1 1 1 1
0 0 1 1 1

0 1 1 1 0
1 1 2 2 0
0 1 2 3 1
0 1 2 3 2
0 0 1 2 3

"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j]：以(i, j)为右下角且只包含 1 的正方形的边长最大值。如果我们能计算出所有
        :param matrix:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare

    def maximalSquare_2nd(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(
                            dp[i][j - 1],
                            dp[i - 1][j],
                            dp[i - 1][j - 1],
                        ) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side ** 2


if __name__ == '__main__':
    s = Solution()
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    res = s.maximalSquare_2nd(matrix)
    print(res)
