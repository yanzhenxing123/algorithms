def solve_sequence_transform():
    """
    解决序列变换问题
    正确理解：每次操作可以选择x和y，将序列a和b中所有等于x的数字都变成y
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
    关键洞察：我们不需要让a变成b，而是让a和b都变成某个相同的目标序列
    """
    # 如果序列已经相同，不需要操作
    if a == b:
        return 0
    
    # 收集所有需要统一的数字
    # 对于每个位置i，如果a[i] ≠ b[i]，我们需要将a[i]和b[i]统一
    transformations = set()
    for i in range(n):
        if a[i] != b[i]:
            transformations.add((a[i], b[i]))
    
    # 如果不需要变换，返回0
    if not transformations:
        return 0
    
    # 使用并查集来管理数字的连通性
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
    # 这意味着它们最终需要变成相同的值
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
    
    # 分析示例1
    print("\n示例1分析:")
    print("a=[3,5,1], b=[2,5,1]")
    print("位置0: a[0]=3, b[0]=2, 需要统一")
    print("位置1: a[1]=5, b[1]=5, 相同")
    print("位置2: a[2]=1, b[2]=1, 相同")
    print("需要统一的数字对: (3,2)")
    print("连通分量数量: 1 (3-2连通)")
    print("操作次数: 1")
    print("但预期输出是0，说明我的理解还有问题...")
    
    # 重新分析示例1
    print("\n重新分析示例1:")
    print("也许题目的意思是：我们需要让a和b都变成某个相同的序列")
    print("对于a=[3,5,1], b=[2,5,1]")
    print("我们可以选择让所有数字都变成5（因为5在两个序列中都存在）")
    print("操作1: 将3变成5")
    print("操作2: 将2变成5")
    print("这样a和b都变成了[5,5,1]")
    print("但这样需要2次操作，不是0...")
    
    print("\n等等！让我重新理解题目...")
    print("也许'完全相同'的意思是：a和b在操作后变成完全相同的序列")
    print("对于示例1，如果我们选择x=3, y=2，那么：")
    print("a中所有3变成2: a=[2,5,1]")
    print("b中所有3变成2: b=[2,5,1]")
    print("这样a和b就完全相同了！")
    print("所以只需要1次操作：选择x=3, y=2")


if __name__ == "__main__":
    # 运行测试
    test_examples()
    print("\n" + "="*50)
    print("运行主程序:")
    print("请输入测试数据:")
    solve_sequence_transform()
