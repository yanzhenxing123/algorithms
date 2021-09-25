"""
@Author: yanzx
@Date: 2021-09-25 08:55:11
@Desc:
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

1 + 1*9 + 2*90 + 3*900 + 4*9000 + ......

"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 1:
            return n
        digit = 0
        pre_pivot = 0
        pivot = 1
        while pivot <= n:
            digit += 1
            pre_pivot = pivot
            pivot = pre_pivot + 9 * digit * 10 ** (digit - 1)

        # 相差的
        delta = (n - pre_pivot) + 1
        # 要加的
        num = delta // digit
        # 从10**n开始的
        start = 10 ** (digit - 1)
        # 找到到达的
        to_num = start + num - 1
        res_flag = delta % digit
        if res_flag == 0:
            return int(str(to_num)[-1])
        end = to_num + 1
        return int(str(end)[res_flag - 1])


if __name__ == '__main__':
    s = Solution()
    res = s.findNthDigit(10)
    print(res)
