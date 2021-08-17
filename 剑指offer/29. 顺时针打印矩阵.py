"""
@Author: yanzx
@Date: 2021/8/17 22:55
@Description:

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],
               [4,5,6],
               [7,8,9]
               ]
输出：[1,2,3,6,9,8,7,4,5]


"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        n = (right+1) * (bottom+1)
        index = 0
        while index < n:
            # 从左到右
            for i in range(left, right+1):
                if index == n:
                    break
                res.append(matrix[top][i])
                index += 1

            top += 1

            # 从上到下
            for i in range(top, bottom+1):
                if index == n:
                    break
                res.append(matrix[i][right])
                index += 1

            right -= 1

            # 从右到左
            for i in range(right, left-1, -1):
                if index == n:
                    break
                res.append(matrix[bottom][i])
                index += 1

            bottom -= 1

            # 从下到上
            for i in range(bottom, top-1, -1):
                if index == n:
                    break
                res.append(matrix[i][left])
                index += 1

            left += 1

        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    s = Solution()
    res = s.spiralOrder(matrix)
    print(res)
