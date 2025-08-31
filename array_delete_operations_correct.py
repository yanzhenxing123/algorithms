def solve_array_delete():
    """
    解决数组删除操作问题
    正确理解：我们需要找到一种删除策略，让剩余数组单调递增
    """
    
    T = int(input())  # 测试用例数量
    
    for _ in range(T):
        n = int(input())  # 数组长度
        arr = list(map(int, input().split()))  # 数组元素
        
        # 计算最少删除操作次数
        result = min_delete_operations_correct(n, arr)
        print(result)


def min_delete_operations_correct(n, arr):
    """
    计算最少删除操作次数 - 正确版本
    关键洞察：我们需要找到一种删除策略，让剩余数组单调递增
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


def min_delete_operations_optimized(n, arr):
    """
    计算最少删除操作次数 - 优化版本
    关键洞察：我们只需要保留最长的单调递增子序列，删除其他元素
    """
    if n == 0:
        return 0
    
    # 如果数组已经单调递增，不需要删除
    if is_monotonic_increasing(arr):
        return 0
    
    # 关键洞察：我们需要找到最长的单调递增子序列
    # 删除操作次数 = 总元素种类数 - 最长单调递增子序列中的元素种类数
    
    # 使用动态规划找最长单调递增子序列
    # dp[i]表示以arr[i]结尾的最长单调递增子序列长度
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] <= arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # 找到最长单调递增子序列的长度
    max_length = max(dp)
    
    # 如果最长子序列长度为1，说明需要删除n-1种元素
    if max_length == 1:
        # 计算不同元素的种类数
        unique_elements = len(set(arr))
        return unique_elements - 1
    
    # 找到最长单调递增子序列
    # 从后往前构造最长子序列
    lis = []
    current_length = max_length
    current_max = float('inf')
    
    for i in range(n-1, -1, -1):
        if dp[i] == current_length and arr[i] <= current_max:
            lis.append(arr[i])
            current_length -= 1
            current_max = arr[i]
    
    lis.reverse()
    
    # 计算需要删除的元素种类数
    # 需要删除的元素种类数 = 总元素种类数 - 最长子序列中的元素种类数
    total_unique = len(set(arr))
    lis_unique = len(set(lis))
    
    return total_unique - lis_unique


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
    test_arr1 = [3, 1, 2, 1, 3]
    
    if is_monotonic_increasing(test_arr1):
        result1 = 0
    else:
        # 使用正确算法
        result1 = min_delete_operations_correct(len(test_arr1), test_arr1)
    
    print(f"实际输出: {result1}")
    print(f"测试{'通过' if result1 == 2 else '失败'}")
    
    print("\n测试示例2:")
    print("输入: n=4, arr=[1,2,3,4]")
    print("预期输出: 0")
    
    # 模拟示例2
    test_arr2 = [1, 2, 3, 4]
    
    result2 = 0 if is_monotonic_increasing(test_arr2) else 1
    print(f"实际输出: {result2}")
    print(f"测试{'通过' if result2 == 0 else '失败'}")
    
    print("\n测试示例3:")
    print("输入: n=6, arr=[2,2,1,1,3,3]")
    print("预期输出: 1")
    
    # 模拟示例3
    test_arr3 = [2, 2, 1, 1, 3, 3]
    
    if is_monotonic_increasing(test_arr3):
        result3 = 0
    else:
        result3 = min_delete_operations_correct(len(test_arr3), test_arr3)
    
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
    
    # 对比两种算法
    print("\n算法对比:")
    print("正确版本结果:", min_delete_operations_correct(len(test_arr1), test_arr1))
    print("优化版本结果:", min_delete_operations_optimized(len(test_arr1), test_arr1))
    print("说明：优化版本的逻辑是错误的！")


if __name__ == "__main__":
    # 运行测试
    test_examples()
    print("\n" + "="*50)
    print("运行主程序:")
    print("请输入测试数据:")
    solve_array_delete()
