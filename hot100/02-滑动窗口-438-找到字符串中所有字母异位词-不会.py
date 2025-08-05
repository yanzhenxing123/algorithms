"""
给定两个字符串 s 和 p，找到 s 中所有 p 的
异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。



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



"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        s：主串
        p：子串
        用子串去初始化s和p，然后再遍历s - p 这个字符串
        维护一个pool，left是窗口的左边界，right是窗口的右边界
        """
        res = []
        s_length, p_length = len(s), len(p)
        if not s or not p or p_length > s_length:
            return res
        # 分别记录每个字符出现的次数
        p_li = [0] * 26
        s_li = [0] * 26
        for i in range(p_length):
            index_p = ord(p[i]) - ord("a")
            index_s = ord(s[i]) - ord("a")
            p_li[index_p] += 1
            s_li[index_s] += 1

        print(f"p_li:     {p_li}")

        if p_li == s_li:
            res.append(0)
        for i in range(p_length, s_length):
            # 维护这个s_li
            index_fast = ord(s[i]) - ord("a")
            index_slow = ord(s[i - p_length]) - ord("a")
            s_li[index_fast] += 1
            s_li[index_slow] -= 1
            print(f"index: {i}, {s_li}")
            if p_li == s_li:  # 说明二者的元素相同
                # print(p_li)
                # print(s_li)
                res.append(i - p_length + 1)
        return res

    def findAnagrams_2nd(self, s: str, p: str) -> List[int]:
        """
        s是主串，p是子串
        """
        s_len, p_len = len(s), len(p)
        if not s_len or not p_len or s_len < p_len:
            return []
        res = []
        s_data = [0] * 26
        p_data = [0] * 26
        for i in range(p_len):
            p_index = ord(p[i]) - ord('a')
            s_index = ord(s[i]) - ord('a')
            p_data[p_index] += 1
            s_data[s_index] += 1
        if s_data == p_data:
            res.append(0)
        for i in range(p_len, len(s)):
            s_left_index = ord(s[i - p_len]) - ord('a')
            s_right_index = ord(s[i]) - ord('a')
            s_data[s_left_index] -= 1
            s_data[s_right_index] += 1
            if s_data == p_data:
                res.append(i - p_len + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.findAnagrams("cbaebabacd", "abc")
    print(res)
