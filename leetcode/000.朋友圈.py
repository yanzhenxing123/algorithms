"""
@Author: yanzx
@Date: 2022/6/4 22:46
@Description:

班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/friend-circles

示例 1：

输入：
[[1,1,0],
[1,1,0],
[0,0,1]]
输出：2
解释：已知学生 0 和学生 1 互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回 2 。
"""

from typing import List



class Solution:
    def findCircles(self, matrix: List[List[int]]) -> int:
        res = 0
        if not matrix:
            return res
        length = len(matrix)
        p = [i for i in range(length)]
        for i in range(length):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    self.union(p, i, j)

        res_li = [self.find_parent(p, i) for i in p]

        return len(set(res_li))

    def find_parent(self, p: List[int], i: int):
        while p[i] != i:
            i = p[i]
        return i

    def union(self, p: List[int], i: int, j: int):
        i_parent = self.find_parent(p, i)
        j_parent = self.find_parent(p, j)
        p[i_parent] = j_parent


if __name__ == '__main__':
    matrix = [[1, 1, 1],
              [1, 1, 0],
              [1, 0, 1]]
    s = Solution()
    res = s.findCircles(matrix)
    print(res)
