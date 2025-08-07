"""
@Time: 2024/3/26 19:54
@Author: yanzx
@Desc:
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。

先放大右边，满足条件，再缩小左边

"""
import copy


class Solution:

    def minWindow_2nd(self, s: str, t: str) -> str:
        """
        滑动窗口
        :param s: 字符串
        :param t: 子串
        :return:
        """

        def check(d: dict):
            '''
            不能用sum，因为有负数
            '''
            # Check if all values in dictionary are <= 0 (meaning we have enough characters)
            for value in d.values():
                if value > 0:
                    return False
            return True

        if not s or len(s) < len(t):
            return ""

        # Create dictionary to count characters in t
        d = {}
        for i in range(len(t)):
            d[t[i]] = d.get(t[i], 0) + 1

        left = 0
        right = 0
        res = ""

        # Initialize the first character
        if s[0] in d:
            d[s[0]] -= 1

        while left <= right and right < len(s):
            if check(d):  # Found a valid window
                # Update result if this is a smaller valid window
                if not res or len(res) > len(s[left: right + 1]):
                    res = s[left: right + 1]

                # Try to shrink window from left
                if s[left] in d:
                    d[s[left]] += 1
                left += 1
            else:  # Need to expand window to right
                right += 1
                if right < len(s) and s[right] in d:
                    d[s[right]] -= 1
        return res

    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for item in t:
            d[item] = d.get(item, 0) + 1
        res = ""
        left, right = 0, 0
        if s[right] in d:
            d[s[right]] -= 1
        while left <= right and right < len(s):
            tmp_str = s[left: right + 1]
            # 判断是否满足条件
            flag = True
            for key, value in d.items():
                if value > 0:
                    flag = False
                    break
            if flag:  # 满足条件收缩左边
                if not res:
                    res = tmp_str
                elif len(res) > len(tmp_str):
                    res = tmp_str
                if s[left] in d:
                    d[s[left]] += 1
                left += 1
            else:  # 扩大右边
                right += 1
                if right < len(s):
                    if s[right] in d:
                        d[s[right]] -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    string = "bba"
    t = "ab"
    res = s.minWindow(string, t)
    print(res)
