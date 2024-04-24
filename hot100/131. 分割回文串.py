"""
@Time: 2024/4/24 09:15
@Author: yanzx
@Desc: 
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.length = len(
            s)
        self.res = []
        self.dfs(s, 1, [])
        return self.res

    def dfs(self, s: str, index: int, path: List[str]):
        print(path)
        if len("".join(path)) == self.length:
            for string in path:
                if not self.is_huiwen(string):
                    return
            self.res.append(path.copy())
            return

        for i in range(index, len(s) + 1):
            path.append(s[:i])
            self.dfs(s[i:], 1, path)
            path.pop()

    def is_huiwen(self, s):
        if not s:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    string = "abcd"
    res = s.partition(string)
    print(res)
