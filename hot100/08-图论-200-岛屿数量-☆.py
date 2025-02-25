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


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # 进行dfs
#         if not grid:
#             return 0
#         row, col = len(grid), len(grid[0])
#         self.row, self.col = row, col
#         res = 0
#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == '1':
#                     res += 1
#                     self.dfs(grid, i, j)
#         return res
#
#     def dfs(self, grid: List[List[str]], i: int, j: int):
#         """
#         上下左右进行dfs
#         """
#         grid[i][j] = '0'  # 已经遍历
#         if i > 0 and grid[i - 1][j] == '1':
#             self.dfs(grid, i - 1, j)
#         if i < self.row - 1 and grid[i + 1][j] == '1':
#             self.dfs(grid, i + 1, j)
#         if j > 0 and grid[i][j - 1] == '1':
#             self.dfs(grid, i, j - 1)
#         if j < self.col - 1 and grid[i][j + 1] == '1':
#             self.dfs(grid, i, j + 1)


if __name__ == '__main__':
    s = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    res = s.numIslands(grid)
    print(res)
