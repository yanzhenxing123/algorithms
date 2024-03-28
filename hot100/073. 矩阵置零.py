"""
@Time: 2024/3/27 14:57
@Author: yanzx
@Desc:
输入：
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
输出：
[[1,0,1],
 [0,0,0],
 [1,0,1]]
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        rows, cols = len(matrix), len(matrix[0])
        d = {
            "col": set(),
            "row": set()
        }
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    d['row'].add(i)
                    d['col'].add(j)
        for i in d['row']:
            for j in range(cols):
                matrix[i][j] = 0

        for j in d['col']:
            for i in range(rows):
                matrix[i][j] = 0


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    res = s.setZeroes(matrix)
    print(res)
