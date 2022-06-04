"""
@Author: yanzx
d@Description: 20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。


eg: '{}(())' is valid
eg: '{}[{]}' is invalid
 
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif item == '(':
                stack.append(')')
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if bracket != item:
                    return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    res = s.isValid("{[]}")
    print(res)