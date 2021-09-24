"""
@Author: yanzx
@Date: 2020/12/19 20:17
@Description: 给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

"""
from typing import List
import copy


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        tmp_arr = [[] for _ in range(length)]
        for i in range(-1, -length-1, -1):
            for j in range(length):
                tmp_arr[j].append(matrix[i][j])

        for i in range(length):
            matrix[i] = tmp_arr[i]


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(matrix)
    print(matrix)



