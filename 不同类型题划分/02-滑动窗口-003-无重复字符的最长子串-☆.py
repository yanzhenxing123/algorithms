"""
@Author: yanzx
@Date: 2021-12-01 13:51:33
@Desc:
输入: s = "abcabcbbaaaaaaaa"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        维护一个窗口 pool
        pool = pool[index + 1: ]
        """
        if not s or len(s) == 1:
            return len(s)

        pool = []
        max_len = 0
        for i in range(len(s)):
            if s[i] in pool:
                index = pool.index(s[i])
                pool = pool[index + 1:]
            pool.append(s[i])
            max_len = max(max_len, len(pool))

        return max_len


# 最优解
class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        inde = -1
        st = {}
        for j in range(len(s)):
            char = [j]
            if s[j] in st:
                i = max(st[s[j]], i)  # 取max是不能让i回去
            max_len = max(max_len, j - i)
            st[s[j]] = j
            print(st)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        最优解，用left记录左端点，且使用for i 中的i记录为右端点
        """
        if not s:
            return 0
        left = 0
        pool = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in pool:
                pool.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(max_len, cur_len)
            pool.add(s[i])
        return max_len


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("aaaa")
    print(res)
