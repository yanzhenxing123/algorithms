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
        st = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i)
            st[s[j]] = j
        return ans


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)
