"""
@Time: 2024/8/22 11:44
@Author: yanzx
@Desc:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        与上题不同的是多了障碍物, 可以将障碍物设置为0即可
        :param obstacleGrid:
        :return:
        """
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                elif obstacleGrid[i][j] == 1:  # 如果有障碍物，则dp设置为0
                    dp[i][j] = 0
                elif i == 0:  # 第一行 或 第一列
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    obstacleGrid = [[1, 0]]

    res = s.uniquePathsWithObstacles(obstacleGrid)
    print(res)
