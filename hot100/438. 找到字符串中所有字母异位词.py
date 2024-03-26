"""
@Time: 2024/3/25 14:53
@Author: yanzx
@Desc:
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

异味词可以使用ascii码

"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        :param s:
        :param p:
        :return:
        """
        res = []
        s_length, p_length = len(s), len(p)
        if not s or not p or p_length > s_length:
            return res
        p_li = [0] * 26
        s_li = [0] * 26
        for i in range(p_length):
            index_p = ord(p[i]) - ord("a")
            index_s = ord(s[i]) - ord("a")
            p_li[index_p] += 1
            s_li[index_s] += 1
        if p_li == s_li:
            res.append(0)
        for i in range(p_length, s_length):
            # 维护这个s_li
            index_fast = ord(s[i]) - ord("a")
            index_slow = ord(s[i - p_length]) - ord("a")
            s_li[index_fast] += 1
            s_li[index_slow] -= 1
            if p_li == s_li:
                res.append(i - p_length + 1)
        return res

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        """
        暴力求解 超出时间限制
        :param s:
        :param p:
        :return:
        """
        res = []
        if not s or not p:
            return res
        s_length, p_length = len(s), len(p)
        p_sorted = "".join(sorted(p))
        for i in range(0, s_length - p_length + 1):
            tmp_str = s[i:i + p_length]
            tmp_sorted_str = "".join(sorted(tmp_str))
            if tmp_sorted_str == p_sorted:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    string = "abab"
    p = "ab"
    res = s.findAnagrams(string, p)
    print(res)
