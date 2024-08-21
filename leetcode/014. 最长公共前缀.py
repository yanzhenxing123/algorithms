"""
@Time: 2024/8/21 18:19
@Author: yanzx
@Desc: 
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        str0 = strs[0]
        prefix_ch_li = list(str0)
        for s in strs[1:]:
            min_length = min(len(s), len(prefix_ch_li))
            j = 0
            while j < min_length:
                if prefix_ch_li[j] != s[j]:
                    break
                j += 1
            prefix_ch_li = prefix_ch_li[:j]
        return "".join(prefix_ch_li)


if __name__ == '__main__':
    s = Solution()
    strs = ["flower", "flow", "flight"]
    res = s.longestCommonPrefix(strs)
    print(res)
