"""
@Author: yanzx
@Date: 2021-10-04 16:55:48
@Desc: 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

                dp[row + 1][col + 1] = max(dp[row][col + 1], dp[row + 1][col]) + grid[row][col]


"""
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]) + 1)]
              for _ in range(len(grid) + 1)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dp[row + 1][col + 1] = max(dp[row][col + 1], dp[row + 1][col]) + grid[row][col]

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    res = s.maxValue(grid)
    print(res)
