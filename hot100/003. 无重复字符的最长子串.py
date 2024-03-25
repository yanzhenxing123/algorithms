"""
@Time: 2024/3/25 10:49
@Author: yanzx
@Desc:

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1. fast=slow，fast往前走
        2. s[fast]在子串中，slow往前走
        3. s[fast]不在子串中，fast往前走
        :param s:
        :return:
        """
        if not s:
            return 0
        fast, slow = 0, 0
        max_length = 1
        while fast < len(s):
            if fast == slow:
                fast += 1
            elif s[fast] in s[slow:fast]:
                i = s[slow:fast].index(s[fast])
                slow = slow + i + 1
            else:
                max_length = max(fast - slow + 1, max_length)
                fast += 1
        return max_length

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        
        """
        st = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)  # 取max是不能让i回去
            ans = max(ans, j - i)
            st[s[j]] = j
            print(st)
        return ans


if __name__ == '__main__':
    s = Solution()
    string = "bbbbb"
    res = s.lengthOfLongestSubstring(string)
    print(res)
