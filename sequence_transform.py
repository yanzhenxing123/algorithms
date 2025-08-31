def solve_sequence_transform():
    """
    解决序列变换问题
    关键洞察：通过分析数字之间的变换关系，找到最少的操作次数
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
    
    # 创建并查集来管理数字的连通性
    parent = list(range(m + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # 分析需要变换的数字对
    transformations = set()
    for i in range(n):
        if a[i] != b[i]:
            # a[i]需要变成b[i]
            transformations.add((a[i], b[i]))
    
    # 如果不需要变换，返回0
    if not transformations:
        return 0
    
    # 构建变换图
    # 对于每个变换(a[i], b[i])，我们需要将a[i]连通到b[i]
    for x, y in transformations:
        union(x, y)
    
    # 计算连通分量的数量
    # 每个连通分量需要一次操作来统一
    components = set()
    for x, y in transformations:
        components.add(find(x))
        components.add(find(y))
    
    # 最少操作次数等于连通分量的数量
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


if __name__ == "__main__":
    # 运行测试
    test_examples()
    print("\n" + "="*50)
    print("运行主程序:")
    print("请输入测试数据:")
    solve_sequence_transform()
