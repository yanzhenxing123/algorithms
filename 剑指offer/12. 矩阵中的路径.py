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
        pass



if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"

    s = Solution()
    res = s.exist(board, word)
    print(res)
