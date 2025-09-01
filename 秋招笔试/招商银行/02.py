"""
@Author: yanzx
@Time: 2025/9/1 19:33 
@Description: 
"""

from collections import deque
class Solution:
    def shortest_path(self, edges, start, end):
        if start == end:
            return 0

        # 构建图，使用邻接表表示
        graph = {}
        for edge in edges:
            u, v = edge
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([(start, 0)])  # 存储员工和当前步数
        visited = set([start])  # 用于记录已访问过的员工

        while queue:
            node, steps = queue.popleft()

            # 遍历当前员工的所有直接连接员工
            for neighbor in graph[node]:
                if neighbor == end:
                    return steps + 1  # 找到目标员工，返回步数
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return -1  # 如果没有找到路径，返回-1


# 示例使用
edges = [["CMB-001", "CMB-002"], ["CMB-002", "CMB-003"], ["CMB-001", "CMB-004"]]
start = "CMB-001"
end = "CMB-003"

solution = Solution()
result = solution.shortest_path(edges, start, end)
print(result)  # 输出：2
