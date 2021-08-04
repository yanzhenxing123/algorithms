"""
@Author: yanzx
@Date: 2021-08-03 12:56:12
@Desc:
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

dfs

"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i: int, j: int, word: str):
            # 终止条件
            if word == "":
                return True

            if i < 0 or i > row-1 or j < 0 or j > col-1:
                return False

            # 如果不等于 终止递归
            if board[i][j] != word[0]:
                return False

            # 将本次走过的路径，用'#'标记
            tmp = board[i][j]
            board[i][j] = "#"

            # 上下左右进行递归
            if dfs(i+1, j, word[1:]):
                return True
            if dfs(i-1, j, word[1:]):
                return True
            if dfs(i, j+1, word[1:]):
                return True
            if dfs(i, j-1, word[1:]):
                return True

            board[i][j] = tmp
            return False

        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                # 每一个都要进行开头
                if dfs(i, j, word):
                    return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"

    s = Solution()
    res = s.exist(board, word)
    print(res)
