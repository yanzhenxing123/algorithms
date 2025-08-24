"""
@Time: 2024/4/27 10:05
@Author: yanzx
@Desc: 不会写

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

测试用例保证输出的长度不会超过 105。



示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        四种不同的情况：
        1. 数字: 转化为整数 multi = multi* 10 + int(c)
        2. 字符：延长当前字符串 res += c
        3. 左括号: 当前状态入栈 stack.append(（数字，总字符）)
        4. 右括号：栈弹出 cur_multi, last_res = stack.pop() ; res = last_res + res * multi

        :param s:
        :return:
        """
        stack = []
        res = ""
        multi = 0
        for c in s:
            if c == '[':
                stack.append((multi, res))
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

