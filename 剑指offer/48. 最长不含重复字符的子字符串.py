"""
@Author: yanzx
@Date: 2021-10-05 12:15:48
@Desc: 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

解题思路：动态规划找出来以s[i]为结尾的最大长度子字符串
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        tmp = res = 0
        for right in range(len(s)):
            left = dic.get(s[right], -1)
            dic[s[right]] = right
            if right - left > tmp:
                tmp = tmp + 1
            else:
                tmp = right - left
            res = max(tmp, res)

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abaaaa")
    print(res)
