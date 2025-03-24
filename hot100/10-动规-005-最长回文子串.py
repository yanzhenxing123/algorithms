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


if __name__ == '__main__':
    s = Solution()
    res = s.longestPalindrome("abccv")
    print(res)
