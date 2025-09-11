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


正指数
x^n= (x^(n/2))^2
负指数:
x^(-n) = 1/(x^n)


计算 2¹⁰：

2¹⁰ = (2⁵)²
2⁵ = (2²)² × 2
2² = (2¹)²
2¹ = (2⁰)² × 2
2⁰ = 1

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        计算x的n次幂（快速幂算法）
        :param x: 底数
        :param n: 指数（可以是正数、负数或零）
        :return: x的n次幂结果
        """

        def quickMul(N: int):
            """
            递归计算x的N次幂（N为非负整数）
            :param N: 非负整数指数
            :return: x的N次幂结果
            """
            # 基本情况：任何数的0次幂都是1
            if N == 0:
                return 1

            # 递归计算x的N//2次幂
            # 这里利用分治思想：x^N = (x^(N/2))^2
            y = quickMul(N // 2)

            # 检查N的奇偶性
            if N % 2 == 0:
                # 如果N是偶数：x^N = (x^(N/2))^2
                return y * y
            else:
                # 如果N是奇数：x^N = (x^(N//2))^2 * x
                return y * y * x

        # 处理指数n的正负情况
        if n >= 0:
            return quickMul(n)
        else:
            # 负指数：x^(-n) = 1/(x^n)
            return 1.0 / quickMul(-n)




if __name__ == '__main__':
    s = Solution()
    res = s.myPow(2, 4)
    print(res)

