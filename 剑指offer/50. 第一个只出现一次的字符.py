"""
@Author: yanzx
@Date: 2021-09-26 16:27:52
@Desc:
输入：s = "abaccdeff"
输出：'b'
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '



if __name__ == '__main__':
    s = Solution()
    res = s.firstUniqChar("abaccdeff")
    print(res)
