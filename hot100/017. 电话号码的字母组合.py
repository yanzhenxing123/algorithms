"""
@Time: 2024/4/20 10:33
@Author: yanzx
@Desc:

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []

        if len(digits) == 1:
            return data[digits]
        elif len(digits) == 2:
            key1, key2 = digits[0], digits[1]
            for i in data[key1]:
                for j in data[key2]:
                    res.append(i + j)
            return res
        elif len(digits) == 3:
            key1, key2, key3 = digits[0], digits[1], digits[2]
            for i in data[key1]:
                for j in data[key2]:
                    for k in data[key3]:
                        res.append(i + j + k)
            return res
        elif len(digits) == 4:
            key1, key2, key3, key4 = digits[0], digits[1], digits[2], digits[3]
            for i in data[key1]:
                for j in data[key2]:
                    for k in data[key3]:
                        for l in data[key3]:
                            res.append(i + j + k + l)
            return res
        else:
            return res


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.data = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        self.res = []
        self.dfs(digits, 0, [])
        return self.res

    def dfs(self, digits: str, index: int, path: List):
        if len(path) == len(digits):
            self.res.append("".join(path))
            return

        for digit in self.data[digits[index]]:
            path.append(digit)
            self.dfs(digits, index + 1, path)
            path.pop()


if __name__ == '__main__':
    s = Solution2()
    res = s.letterCombinations("23")
    print(res)
