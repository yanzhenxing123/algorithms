"""
@Author: yanzx
@Date: 2021/8/2 22:38
@Description:
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

fafa

"""

def main1():
    pass

class Solution:
    def numWays(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        res = 0
        last1, last2 = 1, 1
        for _ in range(2, n):
            res = last2 + last1
            last2 = last1
            last1 = res
        return res % (10 ** 9 + 7)

def test():
    pass

if __name__ == '__main__':
    pass
