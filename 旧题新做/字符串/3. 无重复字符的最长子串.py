"""
@Time: 2024/8/9 14:08
@Author: yanzx
@Desc: 
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        使用字典进行存储
        :param s:
        :return:
        """
        pass



    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        暴力法 空间复杂度为O(1)
        :param s:
        :return:
        """
        if not s or len(s) == 1:
            return len(s)
        fast = slow = 0 # 闭区间
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
