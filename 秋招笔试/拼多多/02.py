"""
@Time: 2025/8/31 16:31
@Author: yanzx
@Description:
3
1 2 3
==
0 1 2

4
4 2 3 1
==
0 1 1 0

"""

from collections import deque


def min_walk_steps(n, a):
    # 初始化距离数组，全部设为-1表示未访问
    dist = [-1] * (n + 1)
    dist[1] = 0  # 起点节点1的步行次数为0

    # 使用队列进行BFS
    queue = deque([1])

    while queue:
        current = queue.popleft()

        # 方式1：使用传送门（不增加步行次数）
        teleport = a[current - 1]  # 注意索引从0开始
        if dist[teleport] == -1:  # 如果传送目标节点未访问
            dist[teleport] = dist[current]
            queue.appendleft(teleport)  # 优先处理传送门，因为步行次数不变

        # 方式2：步行到左边相邻节点（增加1次步行）
        left = current - 1
        if left >= 1 and dist[left] == -1:
            dist[left] = dist[current] + 1
            queue.append(left)

        # 方式3：步行到右边相邻节点（增加1次步行）
        right = current + 1
        if right <= n and dist[right] == -1:
            dist[right] = dist[current] + 1
            queue.append(right)

    # 返回从节点2到节点n的结果（节点1的0已经包含）
    return [dist[i] for i in range(1, n + 1)]


# 读取输入
n = int(input().strip())
a = list(map(int, input().split()))

# 计算并输出结果
result = min_walk_steps(n, a)
print(' '.join(map(str, result)))