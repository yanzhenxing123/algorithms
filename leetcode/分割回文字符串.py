"""
@Author: yanzx
@Date: 2021/3/29 19:27
@Description: 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 判断是否为回文字符串
        def is_pending(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        result = list()
        path = list()

        # 回溯 重点
        def back_track(s, index):
            if index == len(s):
                result.append(path.copy())
                return

            for i in range(index, len(s)): # [0, 3] [1, 3] [2, 3]
                if is_pending(s[index: i+1]):
                    path.append(s[index: i+1])
                    back_track(s, i+1)
                    path.pop()


        back_track(s, 0)

        return result



if __name__ == '__main__':
    s = Solution()
    string = "aab"
    res = s.partition(string)
    print(res)
