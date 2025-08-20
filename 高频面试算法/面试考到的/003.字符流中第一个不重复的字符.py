"""
@Author: yanzx
@Time: 2025/8/20 16:12 
@Description: 
"""


class Solution:
    def __init__(self):
        self.q = []
        self.mp = dict()

    def FirstAppearingOnce(self):
        while len(self.q) != 0:
            # 第一个不重复的字符
            if self.mp[self.q[0]] == 1:
                return self.q[0]
            # 弹出前面的已经重复的字符
            else:
                self.q.pop(0)
        # 都重复了
        return '#'

    def Insert(self, char):
        # 哈希表记录字符出现次数
        if char in self.mp:
            self.mp[char] += 1
        else:
            self.mp[char] = 1
            # 插入字符
            self.q.append(char)