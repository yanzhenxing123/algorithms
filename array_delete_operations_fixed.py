def solve_array_delete():
    """
    解决数组删除操作问题
    重新理解：我们需要找到一种删除策略，让剩余数组单调递增
    """
    
    T = int(input())  # 测试用例数量
    
    for _ in range(T):
        n = int(input())  # 数组长度
        arr = list(map(int, input().split()))  # 数组元素
        
        # 计算最少删除操作次数
        result = min_delete_operations(n, arr)
        print(result)


def min_delete_operations(n, arr):
    """
    计算最少删除操作次数
    重新理解：我们需要找到一种删除策略，让剩余数组单调递增
    """
    if n == 0:
        return 0
    
    # 如果数组已经单调递增，不需要删除
    if is_monotonic_increasing(arr):
        return 0
    
    # 关键洞察：我们需要尝试删除不同的元素组合
    # 找到所有不同的元素值
    unique_values = sorted(set(arr))
    
    # 尝试删除不同的元素组合，找到能让剩余数组单调递增的最少删除次数
    min_deletions = len(unique_values)  # 最坏情况：删除所有元素
    
    # 尝试删除0到len(unique_values)-1种元素
    for delete_count in range(len(unique_values)):
        # 生成所有可能的删除组合
        from itertools import combinations
        
        for delete_values in combinations(unique_values, delete_count):
            # 删除指定的元素值
            remaining = [x for x in arr if x not in delete_values]
            
            # 检查剩余数组是否单调递增
            if is_monotonic_increasing(remaining):
                min_deletions = min(min_deletions, delete_count)
                break
        
        # 如果找到解，提前退出
        if min_deletions <= delete_count:
            break
    
    return min_deletions


def is_monotonic_increasing(arr):
    """
    检查数组是否已经是单调递增的
    """
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True


def test_examples():
    """
    测试示例用例
    """
    print("测试示例1:")
    print("输入: n=5, arr=[3,1,2,1,3]")
    print("预期输出: 2")
    
    # 模拟示例1
    n = 5
    arr = [3, 1, 2, 1, 3]
    
    if is_monotonic_increasing(arr):
        result1 = 0
    else:
        unique_values = sorted(set(arr))
        min_deletions = len(unique_values)
        
        from itertools import combinations
        
        for delete_count in range(len(unique_values)):
            for delete_values in combinations(unique_values, delete_count):
                remaining = [x for x in arr if x not in delete_values]
                if is_monotonic_increasing(remaining):
                    min_deletions = min(min_deletions, delete_count)
                    break
            
            if min_deletions <= delete_count:
                break
        
        result1 = min_deletions
    
    print(f"实际输出: {result1}")
    print(f"测试{'通过' if result1 == 2 else '失败'}")
    
    print("\n测试示例2:")
    print("输入: n=4, arr=[1,2,3,4]")
    print("预期输出: 0")
    
    # 模拟示例2
    n = 4
    arr = [1, 2, 3, 4]
    
    result2 = 0 if is_monotonic_increasing(arr) else 1
    print(f"实际输出: {result2}")
    print(f"测试{'通过' if result2 == 0 else '失败'}")
    
    print("\n测试示例3:")
    print("输入: n=6, arr=[2,2,1,1,3,3]")
    print("预期输出: 1")
    
    # 模拟示例3
    n = 6
    arr = [2, 2, 1, 1, 3, 3]
    
    if is_monotonic_increasing(arr):
        result3 = 0
    else:
        unique_values = sorted(set(arr))
        min_deletions = len(unique_values)
        
        from itertools import combinations
        
        for delete_count in range(len(unique_values)):
            for delete_values in combinations(unique_values, delete_count):
                remaining = [x for x in arr if x not in delete_values]
                if is_monotonic_increasing(remaining):
                    min_deletions = min(min_deletions, delete_count)
                    break
            
            if min_deletions <= delete_count:
                break
        
        result3 = min_deletions
    
    print(f"实际输出: {result3}")
    print(f"测试{'通过' if result3 == 1 else '失败'}")
    
    # 分析示例1
    print("\n示例1分析:")
    print("原数组: [3,1,2,1,3]")
    print("不同元素值: [1,2,3]")
    print("尝试删除策略:")
    print("删除0种元素: [3,1,2,1,3] - 不单调递增")
    print("删除1种元素:")
    print("  删除1: [3,2,3] - 不单调递增")
    print("  删除2: [3,1,1,3] - 不单调递增")
    print("  删除3: [1,2,1] - 不单调递增")
    print("删除2种元素:")
    print("  删除1和2: [3,3] - 单调递增 ✓")
    print("  删除1和3: [2] - 单调递增 ✓")
    print("  删除2和3: [1,1] - 单调递增 ✓")
    print("最少删除操作次数: 2")


if __name__ == "__main__":
    # 运行测试
    test_examples()
    print("\n" + "="*50)
    print("运行主程序:")
    print("请输入测试数据:")
    solve_array_delete()
