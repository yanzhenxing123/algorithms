def solve_sequence_transform():
    """
    解决序列变换问题
    重新理解题目：每次操作可以选择x和y，将序列中所有等于x的数字都变成y
    目标是通过最少的操作让序列a和b变得完全相同
    """
    
    T = int(input())  # 测试用例数量
    
    for _ in range(T):
        n, m = map(int, input().split())  # 序列长度和数字范围
        a = list(map(int, input().split()))  # 序列a
        b = list(map(int, input().split()))  # 序列b
        
        # 计算最少操作次数
        result = min_operations(n, m, a, b)
        print(result)


def min_operations(n, m, a, b):
    """
    计算最少操作次数
    """
    # 如果序列已经相同，不需要操作
    if a == b:
        return 0
    
    # 分析需要变换的数字对
    # 对于每个位置i，如果a[i] ≠ b[i]，我们需要将a[i]变成b[i]
    transformations = set()
    for i in range(n):
        if a[i] != b[i]:
            transformations.add((a[i], b[i]))
    
    # 如果不需要变换，返回0
    if not transformations:
        return 0
    
    # 关键洞察：每次操作可以将所有等于x的数字变成y
    # 我们需要找到最少的操作次数来覆盖所有的变换需求
    
    # 构建变换图：如果a[i]需要变成b[i]，那么a[i]和b[i]之间有一条边
    # 使用并查集来管理连通性
    parent = list(range(m + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # 对于每个变换(a[i], b[i])，将a[i]和b[i]连通
    for x, y in transformations:
        union(x, y)
    
    # 计算连通分量的数量
    # 每个连通分量需要一次操作来统一
    components = set()
    for x, y in transformations:
        components.add(find(x))
        components.add(find(y))
    
    return len(components)


def test_examples():
    """
    测试示例用例
    """
    print("测试示例1:")
    print("输入: n=3, m=8")
    print("a=[3,5,1], b=[2,5,1]")
    print("预期输出: 0")
    
    # 模拟示例1
    n, m = 3, 8
    a = [3, 5, 1]
    b = [2, 5, 1]
    
    # 检查是否已经相同
    if a == b:
        result1 = 0
    else:
        # 分析变换
        transformations = set()
        for i in range(n):
            if a[i] != b[i]:
                transformations.add((a[i], b[i]))
        
        if not transformations:
            result1 = 0
        else:
            # 构建并查集
            parent = list(range(m + 1))
            
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            
            def union(x, y):
                px, py = find(x), find(y)
                if px != py:
                    parent[px] = py
            
            for x, y in transformations:
                union(x, y)
            
            components = set()
            for x, y in transformations:
                components.add(find(x))
                components.add(find(y))
            
            result1 = len(components)
    
    print(f"实际输出: {result1}")
    print(f"测试{'通过' if result1 == 0 else '失败'}")
    
    print("\n测试示例2:")
    print("输入: n=3, m=8")
    print("a=[2,5,1], b=[5,2,1]")
    print("预期输出: 1")
    
    # 模拟示例2
    n, m = 3, 8
    a = [2, 5, 1]
    b = [5, 2, 1]
    
    if a == b:
        result2 = 0
    else:
        transformations = set()
        for i in range(n):
            if a[i] != b[i]:
                transformations.add((a[i], b[i]))
        
        if not transformations:
            result2 = 0
        else:
            parent = list(range(m + 1))
            
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            
            def union(x, y):
                px, py = find(x), find(y)
                if px != py:
                    parent[px] = py
            
            for x, y in transformations:
                union(x, y)
            
            components = set()
            for x, y in transformations:
                components.add(find(x))
                components.add(find(y))
            
            result2 = len(components)
    
    print(f"实际输出: {result2}")
    print(f"测试{'通过' if result2 == 1 else '失败'}")
    
    print("\n测试示例3:")
    print("输入: n=3, m=8")
    print("a=[2,5,2], b=[5,2,1]")
    print("预期输出: 2")
    
    # 模拟示例3
    n, m = 3, 8
    a = [2, 5, 2]
    b = [5, 2, 1]
    
    if a == b:
        result3 = 0
    else:
        transformations = set()
        for i in range(n):
            if a[i] != b[i]:
                transformations.add((a[i], b[i]))
        
        if not transformations:
            result3 = 0
        else:
            parent = list(range(m + 1))
            
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            
            def union(x, y):
                px, py = find(x), find(y)
                if px != py:
                    parent[px] = py
            
            for x, y in transformations:
                union(x, y)
            
            components = set()
            for x, y in transformations:
                components.add(find(x))
                components.add(find(y))
            
            result3 = len(components)
    
    print(f"实际输出: {result3}")
    print(f"测试{'通过' if result3 == 2 else '失败'}")
    
    # 分析示例1
    print("\n示例1分析:")
    print("a=[3,5,1], b=[2,5,1]")
    print("位置0: a[0]=3, b[0]=2, 需要3→2")
    print("位置1: a[1]=5, b[1]=5, 相同")
    print("位置2: a[2]=1, b[2]=1, 相同")
    print("预期输出0，这意味着不需要操作")
    print("这可能意味着题目有其他理解方式...")


if __name__ == "__main__":
    # 运行测试
    test_examples()
    print("\n" + "="*50)
    print("运行主程序:")
    print("请输入测试数据:")
    solve_sequence_transform()
