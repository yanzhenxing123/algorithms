"""
@Author: yanzx
@Date: 2021-10-04 15:13:43
@Desc: 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

if (xi xi-1) 不可以被翻译：
    dp[i] = dp[i-1]
if (xi xi-1) 可以被翻译：
    dp[i] = dp[i-1] + dp[i-2]
"""


class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [1 for _ in range(len(num) + 1)]
        for i in range(1, len(num)):
            if num[i - 1: i + 1] >= "10" and num[i - 1: i + 1] <= "25":
                dp[i + 1] = dp[i] + dp[i - 1]
            else:
                dp[i + 1] = dp[i]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    res = s.translateNum(12258)
    print(res)
