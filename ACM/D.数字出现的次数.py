"""
@Author: yanzx
@Date: 2021/12/11 12:49
@Description:
给定一个整数， 求 的数中, 给定数字的出现次数

觉得这个问题很难啊, 有人提示到 是这个样子的

样例解释
"""


class Solution:
    def numberOf2sInRange(self, n: int, x: int) -> int:
        s = str(n)
        count = 0
        for i in range(len(s)):
            current = int(s[i])
            high = 0 if s[:i] == '' else int(s[:i])
            low = 0 if s[i + 1:] == '' else int(s[i + 1:])
            if current > x:
                count += (high + 1) * (10 ** len(s[i + 1:]))
            elif current < x:
                count += (high) * (10 ** len(s[i + 1:]))
            else:
                count += (high) * (10 ** len(s[i + 1:])) + low + 1
        return count


n, m = map(int, input().split())
nums = list(map(int, input().split()))
for x in nums:
    print(Solution().numberOf2sInRange(n, x))
