"""
@Time: 2024/8/9 14:08
@Author: yanzx
@Desc: 
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        使用字典进行存储
        按照fast遍历，存储
        1. 如过s[fast]不在字典，则存储到字典
        2. 如果s[fast]在字典中，更新slow, 更新字典
        {字符: 索引}
        :param s:
        :return:
        """
        if len(s) <= 1:
            return len(s)
        d = {}
        max_length = 1
        slow = 0
        for fast in range(len(s)):
            if s[fast] not in d:
                d[s[fast]] = fast
            else:
                slow = max(slow, d[s[fast]] + 1) #
                d[s[fast]] = fast
            max_length = max(fast - slow + 1, max_length)
        return max_length

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        暴力法 空间复杂度为O(1)
        :param s:
        :return:
        """
        if not s or len(s) == 1:
            return len(s)
        fast = slow = 0  # 闭区间
        max_length = 1
        while fast < len(s) - 1:
            fast += 1
            if s[fast] in s[slow: fast]:
                i = s[slow: fast].index(s[fast])
                slow = slow + i + 1
            max_length = max(max_length, fast - slow + 1)
        return max_length


if __name__ == '__main__':
    pass
