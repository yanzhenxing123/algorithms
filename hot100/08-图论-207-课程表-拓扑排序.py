"""
@Time: 2024/4/24 23:11
@Author: yanzx
@Desc:
numCourses = 2, prerequisites = [[1,0]]
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses:
            return True
        G = {}
        for i in range(numCourses):
            G[i] = []
        indegrees = [0] * numCourses
        for node0, node1 in prerequisites:  # node1 -> node0
            G[node1].append(node0)
            indegrees[node0] += 1
        stack = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                stack.append(i)
        while stack:
            node = stack.pop()
            indegrees[node] = -1
            for other_node in G[node]:
                indegrees[other_node] -= 1
                if indegrees[other_node] == 0:
                    stack.append(other_node)
        if sum(indegrees) == -1 * numCourses:
            return True
        return False



if __name__ == '__main__':
    s = Solution()
    res = s.canFinish(2, [[1, 0]])
    print(res)
