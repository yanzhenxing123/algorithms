"""
@Author: yanzx
@Date: 2021/8/17 23:30
@Description:
给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        就是这个
        Args:
            n (int): _description_

        Returns:
            List[List[int]]: _description_
        """


        if n == 0:
            return []

        num = 1
        target_index = n*n
        left, right, top, bottom = 0, n-1, 0, n-1
        res = [[0 for _ in range(n)] for _ in range(n)]
        while num <= target_index:
            # 从左到右
            for i in range(left, right+1):
                if num > target_index:
                    break
                res[top][i] = num
                num += 1

            top += 1

            # 从上到下
            for i in range(top, bottom+1):
                if num > target_index:
                    break
                res[i][right] = num
                num += 1
            right -= 1

            # 从右到左
            for i in range(right, left-1, -1):
                if num > target_index:
                    break
                res[bottom][i] = num
                num += 1

            bottom -= 1

            # 从下到上
            for i in range(bottom, top-1, -1):
                if num > target_index:
                    break
                res[i][left] = num
                num += 1

            left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.generateMatrix(3)
    print(res)
