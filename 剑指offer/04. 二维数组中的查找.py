"""
@Author: yanzx
@Date: 2021/8/2 22:21
@Description:
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

# 从右上角看是一颗二叉树

from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        flag = False
        n, m = len(matrix), len(matrix[0])
        row, colomn = 0, m - 1
        while row < n and colomn >= 0:
            root = matrix[row][colomn]
            if root == target:
                flag = True
                break
            if root < target:
                row += 1
            elif root > target:
                colomn -= 1
        return flag


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    s = Solution()
    res = s.findNumberIn2DArray(matrix, -1)
    print(res)
