from collections import deque

def solve_magic_forest():
    """
    解决魔法森林传送门问题
    使用BFS算法找到从节点1到其他所有节点的最少步行次数
    """
    
    # 读取输入
    n = int(input())  # 节点数量
    teleport = list(map(int, input().split()))  # 传送门目标节点列表
    
    # 初始化距离数组，-1表示未访问
    distances = [-1] * (n + 1)
    distances[1] = 0  # 起点到自己的距离为0
    
    # 使用BFS队列
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        current_dist = distances[current]
        
        # 使用传送门（不增加步行次数）
        teleport_target = teleport[current - 1]
        if distances[teleport_target] == -1:  # 传送门目标未访问过
            distances[teleport_target] = current_dist  # 传送门不增加步行次数
            queue.appendleft(teleport_target)  # 优先处理传送门
        
        # 步行到相邻节点
        neighbors = []
        if current > 1:  # 可以步行到左边
            neighbors.append(current - 1)
        if current < n:  # 可以步行到右边
            neighbors.append(current + 1)
        
        # 检查步行邻居
        for neighbor in neighbors:
            if distances[neighbor] == -1:  # 未访问过
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)
    
    # 输出结果（从节点1开始，跳过节点0）
    result = distances[1:n+1]
    print(' '.join(map(str, result)))


def solve_magic_forest_correct():
    """
    正确解决魔法森林传送门问题
    关键洞察：传送门可以让我们到达已经访问过的节点，从而找到更短的路径
    """
    
    # 读取输入
    n = int(input())  # 节点数量
    teleport = list(map(int, input().split()))  # 传送门目标节点列表
    
    # 初始化距离数组，-1表示未访问
    distances = [-1] * (n + 1)
    distances[1] = 0  # 起点到自己的距离为0
    
    # 使用BFS队列
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        current_dist = distances[current]
        
        # 步行到相邻节点
        neighbors = []
        if current > 1:  # 可以步行到左边
            neighbors.append(current - 1)
        if current < n:  # 可以步行到右边
            neighbors.append(current + 1)
        
        # 检查步行邻居
        for neighbor in neighbors:
            if distances[neighbor] == -1:  # 未访问过
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)
        
        # 使用传送门（不增加步行次数）
        teleport_target = teleport[current - 1]
        if distances[teleport_target] == -1:  # 传送门目标未访问过
            distances[teleport_target] = current_dist  # 传送门不增加步行次数
            queue.appendleft(teleport_target)  # 优先处理传送门
    
    # 输出结果（从节点1开始，跳过节点0）
    result = distances[1:n+1]
    print(' '.join(map(str, result)))


def test_examples():
    """
    测试示例用例
    """
    print("测试示例1:")
    print("输入: n=3, teleport=[1,2,3]")
    print("预期输出: 0 1 2")
    
    # 模拟示例1
    n = 3
    teleport = [1, 2, 3]
    
    distances = [-1] * (n + 1)
    distances[1] = 0
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        current_dist = distances[current]
        
        # 步行邻居
        neighbors = []
        if current > 1:
            neighbors.append(current - 1)
        if current < n:
            neighbors.append(current + 1)
        
        for neighbor in neighbors:
            if distances[neighbor] == -1:
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)
        
        # 使用传送门
        teleport_target = teleport[current - 1]
        if distances[teleport_target] == -1:
            distances[teleport_target] = current_dist
            queue.appendleft(teleport_target)  # 优先处理传送门
    
    result1 = distances[1:n+1]
    print(f"实际输出: {' '.join(map(str, result1))}")
    print(f"测试{'通过' if result1 == [0, 1, 2] else '失败'}")
    
    print("\n测试示例2:")
    print("输入: n=5, teleport=[1,2,3,2,5]")
    print("预期输出: 0 1 2 1 2")
    
    # 模拟示例2
    n = 5
    teleport = [1, 2, 3, 2, 5]
    
    distances = [-1] * (n + 1)
    distances[1] = 0
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        current_dist = distances[current]
        
        # 步行邻居
        neighbors = []
        if current > 1:
            neighbors.append(current - 1)
        if current < n:
            neighbors.append(current + 1)
        
        for neighbor in neighbors:
            if distances[neighbor] == -1:
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)
        
        # 使用传送门
        teleport_target = teleport[current - 1]
        if distances[teleport_target] == -1:
            distances[teleport_target] = current_dist
            queue.appendleft(teleport_target)  # 优先处理传送门
    
    result2 = distances[1:n+1]
    print(f"实际输出: {' '.join(map(str, result2))}")
    print(f"测试{'通过' if result2 == [0, 1, 2, 1, 2] else '失败'}")
    
    # 分析示例2的执行过程
    print("\n示例2执行过程分析:")
    print("从节点1开始:")
    print("1 -> 步行到2 (距离1)")
    print("2 -> 传送门到2 (距离1)")
    print("2 -> 步行到3 (距离2)")
    print("3 -> 传送门到3 (距离2)")
    print("3 -> 步行到4 (距离3)")
    print("4 -> 传送门到2 (距离1)")
    print("2 -> 步行到5 (距离2)")


if __name__ == "__main__":
    # 运行测试
    test_examples()
    print("\n" + "="*50)
    print("运行主程序:")
    print("请输入测试数据:")
    solve_magic_forest_correct()
