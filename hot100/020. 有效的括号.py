"""
@Time: 2024/4/22 20:17
@Author: yanzx
@Desc: 
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for item in s:
            if item in {'(', "[", "{"}:
                stack.append(item)
            else:
                if not stack:
                    return False
                item2 = stack.pop()
                if item == ")" and item2 == "(":
                    continue
                if item == "]" and item2 == "[":
                    continue
                if item == "}" and item2 == "{":
                    continue
                return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    string = "()[]{}"
    res = s.isValid(string)
    print(res)
