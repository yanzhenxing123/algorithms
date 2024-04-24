"""
@Time: 2024/4/24 15:45
@Author: yanzx
@Desc:
输入：grid = [[2,1,1],
            [1,1,0],
            [0,1,1]]
输出：4
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
"""
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        q = deque()
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
        res = -1
        while q:
            li = []
            for i in range(len(q)):
                li.append(q.popleft())

            for i, j in li:
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    q.append((i - 1, j))
                if i < row - 1 and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    q.append((i + 1, j))
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    q.append((i, j - 1))
                if j < col - 1 and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    q.append((i, j + 1))
            res += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        if res == -1:
            return 0
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [[2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]]
    res = s.orangesRotting(grid=grid)
    print(res)
