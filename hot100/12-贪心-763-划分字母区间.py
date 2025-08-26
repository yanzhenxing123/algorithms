"""
@Time: 2024/8/21 11:28
@Author: yanzx
@Desc:

给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表


输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        记录每个字母最后出现的次序
        :param s:
        :return:
        """
        last = {}
        for i, ch in enumerate(s):
            if ch not in last:
                last[ch] = i
            else:
                last[ch] = max(i, last[ch])

        end, start = 0, 0
        partition = []
        for i, ch in enumerate(s):
            end = max(end, last[ch])  # 更新区间的end
            if i == end:  # 此区间没有其他元素
                partition.append(end - start + 1)
                start = end + 1
        return partition

    def partitionLabels2(self, s: str) -> List[int]:
        """
        记录每个字母最后出现的次序
        :param s:
        :return:
        """
        last = [0] * 26  # 存储各个字母最后出现的索引
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
        partition = list()
        start = end = 0
        for i, ch in enumerate(s):
            # 1. end每次遇到新的字符的时候，需要更新一个区间最后位置
            end = max(end, last[ord(ch) - ord('a')])
            # 2. 如果i等于end，说明这个区间走到末尾了，那么就可以将这段长度添加到列表中，并且移动到新的区间了
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition


if __name__ == '__main__':
    s = Solution()
    res = s.partitionLabels("abc")
    print(res)
