"""
@Time: 2024/3/22 21:09
@Author: yanzx
@Desc: 49. 字母异位词分组


给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词。


示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]


        使用hash列表



{
    "abc": ["abc", "bca", ...]
}
"""

from typing import List


class Solution:

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

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        data = {}
        res = []
        for s in strs:
            key = "".join(sorted(list(s)))
            if key not in data:
                data[key] = []
            data[key].append(s)
        for value in data.values():
            res.append(value)
        return res

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


def main(a: int):
    return 1


if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = s.groupAnagrams(strs)
    print(res)
