"""
@Author: yanzx
@Time: 2025/9/2 10:58 
@Description:
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。



示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25


提示：

-100.0 < x < 100.0
-231 <= n <= 231-1
n 是一个整数
要么 x 不为零，要么 n > 0 。
-104 <= xn <= 104
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        使用快速幂
        :param x:
        :param n:
        :return:
        """
        def quickMul(N: int):
            """N 是 幂"""
            if N == 0:
                return 1
            y = quickMul(N  // 2)

            if y % 2 == 0:
                return y * y
            else:
                return y * y * x

        if n > 0:
            return quickMul(n)
        else:
            return 1.0 / quickMul(-n)




if __name__ == '__main__':
    s = Solution()
    res = s.myPow(2, 4)
    print(res)

