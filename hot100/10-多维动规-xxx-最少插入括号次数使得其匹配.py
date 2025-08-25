"""
@Author: yanzx
@Description: 非hot100s

给定只包含括号"()[]{}"的字符串，问最少需要插入多少个括号使该字符串合法匹配。

"""

from typing import List


def min_insertions_to_make_valid(s):
    """
    计算最少需要插入多少个括号使字符串合法匹配

    Args:
        s: 输入字符串，只包含 "()[]{}"

    Returns:
        最少插入的括号数量
    """
    n = len(s)
    if n == 0:
        return 0

    # dp[i][j] 表示处理子串 s[i...j] 所需的最少插入次数
    dp = [[0] * n for _ in range(n)]

    # 初始化：单个字符需要插入一个匹配的括号
    for i in range(n):
        dp[i][i] = 1

    # 自底向上填充dp表
    for length in range(2, n + 1):  # 子串长度从2开始
        for i in range(n - length + 1):  # 子串起始位置
            j = i + length - 1  # 子串结束位置

            # 情况1：如果s[i]和s[j]匹配
            if is_matching(s[i], s[j]):
                dp[i][j] = dp[i + 1][j - 1]
            else:
                # 情况2：s[i]和s[j]不匹配，考虑分割和插入
                # 2a: 分割子串
                min_split = float('inf')
                for k in range(i, j):
                    min_split = min(min_split, dp[i][k] + dp[k + 1][j])

                # 2b: 插入括号
                min_insert = min(dp[i + 1][j] + 1, dp[i][j - 1] + 1)

                # 取两种情况的最小值
                dp[i][j] = min(min_split, min_insert)

    return dp[0][n - 1]


def is_matching(left, right):
    """判断两个括号是否匹配"""
    return (left == '(' and right == ')') or \
        (left == '[' and right == ']') or \
        (left == '{' and right == '}')


# 测试函数
def test_solution():
    """测试解决方案"""

    test_cases = [
        "()",  # 已经匹配，需要0个
        "(",  # 需要1个
        ")",  # 需要1个
        "()[]{}",  # 已经匹配，需要0个
        "([{}])",  # 已经匹配，需要0个
        "([)]",  # 需要2个
        "(((",  # 需要3个
        ")))",  # 需要3个
        "([{}",  # 需要1个
        "([{}])",  # 已经匹配，需要0个
        "((()",  # 需要1个
        "(()))",  # 需要1个
        "([)]",  # 需要2个
        "{[()]}",  # 已经匹配，需要0个
        "{[()",  # 需要1个
    ]

    print("=== 括号匹配问题测试 ===")
    print("字符串\t\t最少插入数量")
    print("-" * 30)

    for s in test_cases:
        result = min_insertions_to_make_valid(s)
        print(f"{s:<12}\t{result}")

    return test_cases


# 运行测试
test_cases = test_solution()


class Solution:
    def minInsertions(self, s: str) -> int:
        """
        dp[i][j]表示处理子串 s[i..j]所需的最少插入次数，也就是s[i:j+1]
        :param s:
        :return:
        """
        if not s or len(s) == 1:
            return len(s)
        n = len(s)

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if (s[i] == '(' and s[j] == ')') or \
                        (s[i] == '[' and s[j] == ']') or \
                        (s[i] == '{' and s[j] == '}'):

                    dp[i][j] = dp[i + 1][j - 1]

                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

                for k in range(i, j):
                    dp[j][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]


if __name__ == '__main__':
    s = Solution()
    string = "()))(("

    res = s.minInsertions(string)
    print(res)
