"""
@Time: 2024/4/27 10:05
@Author: yanzx
@Desc: 不会写
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
            print(stack)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.decodeString("3[a]2[bc]")
    print(res)

