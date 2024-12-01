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
        # if len(s) <= 1:
        #     return len(s)
        # d = {}
        # max_length = 11   `
        # slow = 0
        # for fast in range(len(s)):
        #     if s[fast] not in d:
        #         d[s[fast]] = fast
        #     else:
        #         slow = max(slow, d[s[fast]] + 1)  #
        #         d[s[fast]] = fast
        #     max_length = max(fast - slow + 1, max_length)
        # return max_length

        length = len(s)
        if length <= 1:
            return length
        char2maxIndex = {}  # 存储每个字符串最大的index
        left = 0  # 记左边字符串的索引
        max_length = 1
        for i in range(length):
            # 便利存储
            cur_char = s[i]
            if cur_char in char2maxIndex:
                left = max(char2maxIndex[cur_char] + 1, left)  # 取max是因为可能要更新的字符串已经在left的left了
            char2maxIndex[cur_char] = i
            max_length = max(i - left + 1, max_length)
        return max_length

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        暴力法 空间复杂度为O(1)
        :param s:
        :return:
        """
        length = len(s)
        if length <= 1:
            return length
        # 维护一个没有重复字符串的pool
        pool = []
        pool.append(s[0])
        max_length = 1
        for i in range(1, length):
            cur_char = s[i]
            if cur_char in pool:
                index = pool.index(cur_char)
                pool = pool[index + 1:]
            pool.append(cur_char)
            max_length = max(max_length, len(pool))
        return max_length


if __name__ == '__main__':
    pass
