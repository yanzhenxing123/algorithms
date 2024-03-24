"""
@Time: 2024/3/22 21:09
@Author: yanzx
@Desc: 49. 字母异位词分组

        使用hash列表


{
"abc": ["abc", "bca", ...]
}
"""

from typing import List


class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        """
        使用矩阵形式
        """
        if not strs:
            return [[""]]
        if len(strs) == 1:
            return [strs]

        res = []
        flags = [0 for _ in range(len(strs))]
        for i in range(len(strs)):
            if flags[i]:
                continue
            tmp_set = set()
            sorted_str_i = "".join(sorted(strs[i]))
            tmp_set.add(sorted_str_i)
            li = [strs[i]]
            for j in range(i + 1, len(strs)):
                if len(strs[j]) != len(strs[i]):
                    continue
                sorted_str_j = "".join(sorted(strs[j]))
                if sorted_str_j in tmp_set:
                    li.append(strs[j])
                    flags[j] = 1
            res.append(li)
        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        使用hash列表
        """
        if not strs:
            return [[""]]
        res = []
        flags = [0 for _ in range(len(strs))]
        d = {}
        for i in range(len(strs)):
            if flags[i]:
                continue
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str not in d:
                d[sorted_str] = [strs[i]]
            else:
                d[sorted_str].append(strs[i])

        for _, value in d.items():
            res.append(value)
        return res


def main(a: int):
    return 1


if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = s.groupAnagrams(strs)
    print(res)
