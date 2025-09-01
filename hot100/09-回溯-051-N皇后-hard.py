"""
@Time: 2024/4/24 10:21
@Author: yanzx
@Desc:

不能同行
不能同列
不能同斜线

[
    [1, 1, 1, 1],
    [1, 1, 1, 1]
    [1, 1, 1, 1]
    [1, 1, 1, 1]
] eg: (0, 1) (1, 2) => row - column是否一样



同一个斜线：
    1. 左上到右下：(0, 1) (1, 2) => row - column是否一样
    2. 右上到左下：(0, 2) (1, 1) => row + column是否一样



"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []  # 存储最终结果的二维字符串数组
        chessboard = ['.' * n for _ in range(n)]  # 初始化棋盘 # ['....', '....', '....', '....']
        self.backtracking(n, 0, chessboard, result)  # 回溯求解
        return [[''.join(row) for row in solution] for solution in result]  # 返回结果集

    def backtracking(self, n: int, row: int, chessboard: List[str], result: List[List[str]]) -> None:
        if row == n:
            result.append(chessboard[:])  # 棋盘填满，将当前解加入结果集
            return

        for col in range(n):
            if self.isValid(row, col, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col + 1:]  # 放置皇后
                self.backtracking(n, row + 1, chessboard, result)  # 递归到下一行
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col + 1:]  # 回溯，撤销当前位置的皇后

    def isValid(self, row: int, col: int, chessboard: List[str]) -> bool:
        # 检查列
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False  # 当前列已经存在皇后，不合法

        # 检查 45 度角是否有皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1

        return True  # 当前位置合法


class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:  # 递归终止的条件
                board = generateBoard()
                solutions.append(board)
            else:
                # (row, i)是当前位置¬
                for i in range(n):  # 对列进行遍历
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:  # 同一列或者个斜线
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions


if __name__ == '__main__':
    s = Solution()
    res = s.solveNQueens(4)
    print(res)
