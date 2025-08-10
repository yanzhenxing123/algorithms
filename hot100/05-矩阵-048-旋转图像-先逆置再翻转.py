"""
@Time: 2024/3/27 20:08
@Author: yanzx
@Desc:

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

输入：matrix =
[[1,2,3],
[4,5,6],
[7,8,9]]

逆置：
1 4 7
2 5 8
3 6 9
每行再翻转
7 4 1
8 5 2
9 6 3
输出：
[[7,4,1],
[8,5,2],
[9,6,3]]
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        先逆置，再翻转
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        # 1. 先逆置
        for i in range(row):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. 每行翻转
        for i in range(row):
            left, right = 0, col - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
                
    def rotate(self, matrix: List[List[int]]) -> None:

                


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    res = s.rotate(matrix)
    print(matrix)