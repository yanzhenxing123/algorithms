"""
@Author: yanzx
@Date: 2021/3/29 16:37
@Description:
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小值
输入：grid = [[1,3,1],\
            [1,5,1],
            [4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。



"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[row-1][col-1]


if __name__ == '__main__':

    s = Solution()

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = s.minPathSum(grid)
    print(res)


