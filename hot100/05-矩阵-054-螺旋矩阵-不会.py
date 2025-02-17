"""
@Time: 2024/3/27 15:30
@Author: yanzx
@Desc:
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

输入：matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]


输入：matrix = [[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

不会
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        模拟这个即可
        关键是如何去遍历
        # 从左到右
        d
        for i in range(left, right + 1):
            if index == n:
                break
            res.append(matrix[top][i])
            index += 1
        top += 1

        :param matrix:
        :return:
        """
        res = []
        if not matrix:
            return res
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        n = (right + 1) * (bottom + 1)
        index = 0
        while index < n:
            # 从左到右
            for i in range(left, right + 1):
                if index == n:
                    break
                res.append(matrix[top][i])
                index += 1

            top += 1

            # 从上到下
            for i in range(top, bottom + 1):
                if index == n:
                    break
                res.append(matrix[i][right])
                index += 1

            right -= 1

            # 从右到左
            for i in range(right, left - 1, -1):
                if index == n:
                    break
                res.append(matrix[bottom][i])
                index += 1

            bottom -= 1

            # 从下到上
            for i in range(bottom, top - 1, -1):
                if index == n:
                    break
                res.append(matrix[i][left])
                index += 1

            left += 1

        return res


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = s.spiralOrder(matrix)
    print(res)
