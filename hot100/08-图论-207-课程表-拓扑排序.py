"""
@Time: 2024/4/24 23:11
@Author: yanzx
@Desc:
numCourses = 2, prerequisites = [[1,0]]



你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """拓扑排序
        1. 使用邻接表构建有向图
        2. 遍历删除节点

        Args:
            numCourses (int): _description_
            prerequisites (List[List[int]]): _description_

        Returns:
            bool: _description_
        """

        if not numCourses:
            return True
        G = {}
        for i in range(numCourses):
            G[i] = [] # 表示节点i的出度有哪些
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
    
    def canFinish_2nd(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """列表中每个元素(i, j) j -> i

        Args:
            numCourses (int): _description_
            prerequisites (List[List[int]]): _description_

        Returns:
            bool: _description_
        """
        if not numCourses or not prerequisites:
            return True
        # 1. 创建邻接表
        G = {}
        indegree = [0] * numCourses
        for i in range(numCourses):
            G[i] = []
        # 2. 构造图，更新入度
        for prerequisite in prerequisites:
            i, j = prerequisite
            G[j].append(i)
            indegree[i] += 1
        # 3. 入度为0的节点
        stack = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)
        # 4. 更新
        while stack:
            node = stack.pop()
            node_points = G[node]
            for i in node_points:
                indegree[i] -= 1
                if indegree[i] == 0:
                    stack.append(i)
        if sum(indegree) == 0:
            return True
        return False













if __name__ == '__main__':
    s = Solution()
    res = s.canFinish(2, [[1, 0]])
    print(res)
