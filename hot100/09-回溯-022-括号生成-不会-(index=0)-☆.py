"""
@Time: 2024/4/22 14:22
@Author: yanzx
@Desc: 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。


示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.dfs(n, [])
        return self.res

    def is_valid(self, string: str) -> bool:
        """
        判断括号是否合法
        :param path:
        :return:
        """
        li = []
        for i in string:
            if i == "(":
                li.append(i)
            else:
                if not li:
                    return False
                j = li.pop()
                if i == j:
                    return False
        if li:
            return False
        return True

    def dfs(self, n: int, path: List[str]):
        if len(path) == n * 2:
            string = "".join(path)
            if self.is_valid(string):
                self.res.append(string)
            print(string, self.is_valid(string))
            return
        for i in "()":
            path.append(i)
            if path[0] == ")":
                path.pop()
                break
            self.dfs(n, path)
            path.pop()

    def generateParenthesis_2nd(self, n: int) -> List[str]:
        """
        需要写一个判断括号是否合法的函数
        :param n:
        :return:
        """

        def is_valid(string: str) -> bool:
            if not string:
                return True
            li = []
            for s in string:
                if s == '(':
                    li.append(s)
                elif s == ')':
                    if not li:
                        return False
                    top_s = li.pop()
                    if s == top_s:
                        return False
            if li:
                return False
            return True

        def dfs(s_li: List, index: int, path: List):
            if len(path) == 2 * n:
                string = "".join(path)
                if is_valid(string):
                    res.append(string)
                return

            for i in range(len(s_li)):
                path.append(s_li[i])
                if path[0] == ')':
                    path.pop()
                    return
                dfs(s_li, 0, path)
                path.pop()

        res = []

        dfs(['(', ')'], 0, [])

        return res


if __name__ == '__main__':
    n = 3
    s = Solution()
    res = s.generateParenthesis_2nd(n)
    print(res)
