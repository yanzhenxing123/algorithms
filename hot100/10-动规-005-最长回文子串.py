"""
@Author: yanzx
@Date: 2025/3/8 10:46
@Description:
给你一个字符串 s，找到 s 中最长的 回文 子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        一定要写出来
        :param s:
        :return:
        """
        # 中心扩展法 O(n^2)
        max_right = 0
        max_left = 0
        # 以一个字母为中心
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            while left != -1 and right != len(s) and s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_left = left
                    max_right = right
                left -= 1
                right += 1
        # 以空洞为中心
        for i in range(len(s) - 1):
            left = i
            right = i + 1
            while left != -1 and right != len(s) and s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_left = left
                    max_right = right
                left -= 1
                right += 1
        return s[max_left: max_right + 1]

    def longestPalindrome_2nd(self, s: str) -> str:
        if len(s) <= 1:
            return s
        # 1. 遍历字母为中心
        max_left, max_right = 0, 0
        for i in range(1, len(s)):
            left, right = i - 1, i + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_left = left
                    max_right = right
                left -= 1
                right += 1

        # 2. 遍历空洞为中心
        for i in range(0, len(s)):
            left, right = i, i + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if right - left > max_right - max_left:
                    max_left = left
                    max_right = right
                left -= 1
                right += 1

        return s[max_left: max_right + 1]

    def longestPalindrome_dp(self, s: str) -> str:
        """
        使用动态规划方法
        :param s:
        :return:
        """
        n = len(s)
        if n < 2:
            return s

        # 初始化 dp 表
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1  # 初始化为第一个字符，长度为1

        # 单个字符一定是回文
        for i in range(n):
            dp[i][i] = True

        # 填表，按子串长度从小到大
        for length in range(2, n + 1):  # 子串长度从2到n
            for i in range(n):  # 子串起始位置
                j = i + length - 1  # 子串结束位置
                if j >= n:  # 越界检查
                    break
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > max_len:
                            start = i
                            max_len = length
        return s[start:start + max_len]


if __name__ == '__main__':
    s = Solution()
    res = s.longestPalindrome("abccv")
    print(res)
