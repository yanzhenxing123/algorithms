"""
@Time: 2025/3/24 11:02
@Author: yanzx
@Desc: 关键是如何解决问题
"""
import numpy as np


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return a % 1e9 + 7

    def fibonacci_matrix(self, n):
        def matrix_power(matrix, power):
            result = np.identity(2, dtype=object)
            while power > 0:
                if power % 2 == 1:
                    result = np.dot(result, matrix)
                matrix = np.dot(matrix, matrix)
                power = power // 2
            return result

        if n <= 1:
            return n
        F = np.array([[1, 1], [1, 0]], dtype=object)
        result_matrix = matrix_power(F, n - 1)
        return result_matrix[0][0]


if __name__ == '__main__':
    s = Solution()
    res = s.fibonacci_matrix(5)
    print(res)
