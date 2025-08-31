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
    关键洞察：我们需要让a和b通过一系列操作后变得完全相同
    这意味着我们需要找到最少的操作次数来统一所有相关的数字
    """
    # 如果序列已经相同，不需要操作
    if a == b:
        return 0
    
    # 分析需要统一的数字
    # 我们需要让a和b中所有相关的数字都变成相同的值
    
    # 收集所有需要统一的数字
    all_numbers = set()
    for i in range(n):
        all_numbers.add(a[i])
        all_numbers.add(b[i])
    
    # 如果只有一个数字，不需要操作
    if len(all_numbers) == 1:
        return 0
    
    # 关键洞察：每次操作可以将所有等于x的数字变成y
    # 我们需要找到最少的操作次数来统一所有数字
    
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
    
    # 对于每个位置i，如果a[i] ≠ b[i]，我们需要将a[i]和b[i]连通
    # 这意味着它们最终需要变成相同的值
    for i in range(n):
        if a[i] != b[i]:
            union(a[i], b[i])
    
    # 计算连通分量的数量
    # 每个连通分量需要一次操作来统一
    components = set()
    for num in all_numbers:
        components.add(find(num))
    
    # 最少操作次数等于连通分量的数量减1
    # 因为我们可以选择其中一个连通分量作为目标值
    return len(components) - 1


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
        # 收集所有数字
        all_numbers = set()
        for i in range(n):
            all_numbers.add(a[i])
            all_numbers.add(b[i])
        
        if len(all_numbers) == 1:
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
            
            # 连通需要统一的数字
            for i in range(n):
                if a[i] != b[i]:
                    union(a[i], b[i])
            
            # 计算连通分量
            components = set()
            for num in all_numbers:
                components.add(find(num))
            
            result1 = len(components) - 1
    
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
        all_numbers = set()
        for i in range(n):
            all_numbers.add(a[i])
            all_numbers.add(b[i])
        
        if len(all_numbers) == 1:
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
            
            for i in range(n):
                if a[i] != b[i]:
                    union(a[i], b[i])
            
            components = set()
            for num in all_numbers:
                components.add(find(num))
            
            result2 = len(components) - 1
    
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
        all_numbers = set()
        for i in range(n):
            all_numbers.add(a[i])
            all_numbers.add(b[i])
        
        if len(all_numbers) == 1:
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
            
            for i in range(n):
                if a[i] != b[i]:
                    union(a[i], b[i])
            
            components = set()
            for num in all_numbers:
                components.add(find(num))
            
            result3 = len(components) - 1
    
    print(f"实际输出: {result3}")
    print(f"测试{'通过' if result3 == 2 else '失败'}")
    
    # 分析示例1
    print("\n示例1分析:")
    print("a=[3,5,1], b=[2,5,1]")
    print("位置0: a[0]=3, b[0]=2, 需要统一")
    print("位置1: a[1]=5, b[1]=5, 相同")
    print("位置2: a[2]=1, b[2]=1, 相同")
    print("数字集合: {3,2,5,1}")
    print("需要统一的数字对: (3,2)")
    print("连通分量数量: 3 (3-2连通, 5独立, 1独立)")
    print("操作次数: 3-1 = 2")
    print("但预期输出是0，说明我的理解还有问题...")


if __name__ == "__main__":
    # 运行测试
    test_examples()
    print("\n" + "="*50)
    print("运行主程序:")
    print("请输入测试数据:")
    solve_sequence_transform()
