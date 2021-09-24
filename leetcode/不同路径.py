"""
@Author: yanzx
@Date: 2020/12/20 12:12
@Description:

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        matrix[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] = matrix[i][j - 1]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[i][j]


if __name__ == '__main__':
    s = Solution()
    res = s.uniquePaths(1, 2)
    print(res)
