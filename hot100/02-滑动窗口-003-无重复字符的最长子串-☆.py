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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        最优解，用left记录左端点，且使用for i 中的i记录为右端点
        并且pool中只包含 left：i 中的所有字符串，且不重复
        """
        if not s:
            return 0
        left = 0
        pool = set()
        n = len(s)
        max_len = 0
        for i in range(n):
            while s[i] in pool:  # 保证当前元素不存在set中 也就是找到最左边不是当前元素的元素 也就是维护一个公共低劣d
                pool.remove(s[left])
                left += 1
            pool.add(s[i])
            max_len = max(max_len, len(pool))
        return max_len

    def lengthOfLongestSubstring_2nd(self, s: str) -> int:
        max_len = 0
        if not s or len(s) == 1:
            return 1
        left = 0
        pool = set()
        for i in range(len(s)):
            while s[i] in pool:
                pool.remove(s[left])
                left += 1
            pool.add(s[i])
            max_len = max(len(pool), max_len)
        return max_len

    def lengthOfLongestSubstring_3st(self, s: str) -> int:
        if not s or len(s) == 1:
            return len(s)
        res = 0
        left = 0
        pool = set()
        for i in range(len(s)):
            while s[i] in pool:  # 当前要加入的元素一定不在pool中
                pool.remove(s[left])
                left += 1
            pool.add(s[i])
            res = max(len(pool), res)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("aaaa")
    print(res)
