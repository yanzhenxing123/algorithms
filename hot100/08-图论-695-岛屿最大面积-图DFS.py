"""
@Time: 2024/4/24 15:20
@Author: yanzx
@Desc: 图的遍历
给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。


[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
"""

from typing import List



class Solution:
    def __init__(self):
        self.res = 0
        self.cur_area = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(grid, i, j):

            self.cur_area += 1
            self.res = max(self.res, self.cur_area)

            grid[i][j] = 0

            if i > 0 and grid[i-1][j] == 1:
                dfs(grid, i-1, j)
            if i < rows - 1 and grid[i+1][j] == 1:
                dfs(grid, i+1, j)
            if j > 0 and grid[i][j-1] == 1:
                dfs(grid, i, j-1)
            if j < cols - 1 and grid[i][j+1] == 1:
                dfs(grid, i, j+1)

        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.cur_area = 0
                    dfs(grid, i, j)

        return self.res






if __name__ == '__main__':
    s = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    res = s.numIslands_3rd(grid)
    print(res)
