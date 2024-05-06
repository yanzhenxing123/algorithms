"""
@Time: 2024/4/27 11:34
@Author: yanzx
@Desc: 栈相关
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        stack中存储下标
        :param temperatures:
        :return:
        """
        res = [0] * len(temperatures)
        stack = []
        if not temperatures:
            return [0]
        stack.append(0)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    res = s.dailyTemperatures(temperatures)
    print(res)
