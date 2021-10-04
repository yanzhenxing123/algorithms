"""
@Author: yanzx
@Date: 2021-10-04 19:15:02
@Desc: 
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        res = s.split()
        res.reverse()
        return " ".join(res)