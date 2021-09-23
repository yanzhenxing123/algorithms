"""
@Author: yanzx
@Date: 2021-09-23 16:50:48
@Desc:
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
eg1:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""
from typing import List
from itertools import permutations


class Solution1:
    def permutation(self, s: str) -> List[str]:
        res_tuple = list(permutations(s))
        for i in range(len(res_tuple)):
            res_tuple[i] = "".join(res_tuple[i])
        return list(set(res_tuple))


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = set()
        visited = [False for _ in range(len(s))]

        def dfs(s: str, path: str, visited: list):
            if len(path) == len(s):
                res.add(path)
                return

            for i in range(len(s)):
                if visited[i]:
                    continue
                path += s[i]
                visited[i] = True
                dfs(s, path, visited)
                visited[i] = False
                path = path[:len(path) - 1]

        dfs(s, "", visited)
        return list(res)


if __name__ == '__main__':
    s = Solution()
    res = s.permutation("abc")
    print(res)
