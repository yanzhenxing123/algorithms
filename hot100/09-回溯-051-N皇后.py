"""
@Time: 2024/4/24 10:21
@Author: yanzx
@Desc:

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
        self.n = n
        self.columns = set()
        self.diags1 = set()
        self.diags2 = set()
        self.res = []
        self.row_board = ["."] * self.n
        self.dfs(0, [])
        return self.res

    def dfs(self, row: int, path: List[int]):
        """
        一层递归就是一行
        :param row: 开始的行
        :return:
        """
        if row == self.n:  # 说明满足条件
            board = self.get_board(path)
            self.res.append(board)
            return

        for i in range(self.n):  # i是列
            if i in self.columns or row + i in self.diags1 or row - i in self.diags2:
                continue
            self.columns.add(i)
            path.append(i)
            self.diags1.add(row + i)
            self.diags2.add(row - i)
            self.dfs(row + 1, path)
            self.diags2.remove(row - i)
            self.diags1.remove(row + i)
            path.pop()
            self.columns.remove(i)

    def get_board(self, path):
        board = []
        for column in path:
            self.row_board[column] = "Q"
            row_board_str = "".join(self.row_board)
            board.append(row_board_str)
            self.row_board[column] = "."
        return board


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
