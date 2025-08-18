"""
@Time: 2024/4/24 15:20
@Author: yanzx
@Desc: 图的遍历
相当于查找图的联通分量的个数

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
"""

from typing import List


class Solution:
    """重新写一遍，比较重要"""

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, row, col, i, j):
            grid[i][j] = '0'
            # 上下左右去回溯
            if i > 0 and grid[i - 1][j] == '1':
                dfs(grid, row, col, i - 1, j)
            if i < row - 1 and grid[i + 1][j] == '1':
                dfs(grid, row, col, i + 1, j)
            if j > 0 and grid[i][j - 1] == '1':
                dfs(grid, row, col, i, j - 1)
            if j < col - 1 and grid[i][j + 1] == '1':
                dfs(grid, row, col, i, j + 1)

        res = 0
        row = len(grid)
        if not row:
            return 0
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(grid, row, col, i, j)
                    res += 1
        return res

    def numIslands_2nd(self, grid: List[List[str]]) -> int:
        """
        二刷，其实就是联通分量的数量
        :param grid:
        :return:
        """

        def dfs(grid: List[List[str]], i: int, j: int):
            grid[i][j] = '0'
            m, n = len(grid), len(grid[0])

            # 上下左右回溯
            if i > 0 and grid[i - 1][j] == '1':
                dfs(grid, i - 1, j)
            if i < m - 1 and grid[i + 1][j] == '1':
                dfs(grid, i + 1, j)
            if j > 0 and grid[i][j - 1] == '1':
                dfs(grid, i, j - 1)
            if j < n - 1 and grid[i][j + 1] == '1':
                dfs(grid, i, j + 1)
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1
        return res

    def numIslands_3rd(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            grid[i][j] = '0'
            # 上下左右递归操作
            if i > 0 and grid[i-1][j] == '1':
                dfs(grid, i-1, j)
            if i < rows - 1 and grid[i + 1][j] == '1':
                dfs(grid, i+1, j)
            if j > 0 and grid[i][j-1] == '1':
                dfs(grid, i, j-1)
            if j < cols-1 and grid[i][j+1] == '1':
                dfs(grid, i, j+1)

        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res += 1
                    
        return res


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
