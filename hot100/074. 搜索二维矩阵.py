"""
@Time: 2024/4/25 23:29
@Author: yanzx
@Desc: 
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        :param matrix:
        :param target:
        :return:
        """
        if not matrix:
            return False
        row_left, row_right = 0, len(matrix[0]) - 1
        col_left, col_right = 0, len(matrix) - 1
        # 1. 先找到在哪一列
        while row_left <= row_right:
            mid = (row_left + row_right) // 2
            if matrix[0][mid] < target:
                row_left = mid + 1
            elif matrix[0][mid] > target:
                row_right = mid - 1
            else:
                return True
        # 最终row_left为插入位置，即比target大
        if row_left == 0:
            return False
        # 2. 按照列查找
        col = row_left - 1
        # 看一下这一列有没有
        while col_left <= col_right:
            mid = (col_left + col_left) // 2
            if matrix[mid][col] < target:
                col_left = mid + 1
            elif matrix[mid][col] > target:
                col_right = mid - 1
            else:
                return True

        row_left, row_right = 0, len(matrix[0]) - 1
        col_left, col_right = 0, len(matrix) - 1
        # 1. 先找到在哪一行
        while col_left <= col_right:
            mid = (col_left + col_left) // 2
            if matrix[mid][0] < target:
                col_left = mid + 1
            elif matrix[mid][0] > target:
                col_right = mid - 1
            else:
                return True
        if col_left == 0:
            return False
        row = col_left - 1
        while row_left <= row_right:
            mid = (row_left + row_right) // 2
            if matrix[row][mid] < target:
                row_left = mid + 1
            elif matrix[row][mid] > target:
                row_right = mid - 1
            else:
                return True
        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        """
        按行按照列都是有序, 右上角看是一棵二叉树
        :param matrix:
        :param target:
        :return:
        """
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        while i < row and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    s = Solution()
    res = s.searchMatrix(matrix, target=10)
    print(res)
