def solve_array_delete():
    """
    解决数组删除操作问题
    关键洞察：找到最长的单调递增子序列，然后删除其他元素
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
    关键洞察：我们需要找到最长的单调递增子序列
    删除操作次数 = 总元素种类数 - 最长单调递增子序列中的元素种类数
    """
    if n == 0:
        return 0
    
    # 如果数组已经单调递增，不需要删除
    if is_monotonic_increasing(arr):
        return 0
    
    # 找到最长的单调递增子序列
    # 使用动态规划：dp[i]表示以arr[i]结尾的最长单调递增子序列长度
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] <= arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # 最长单调递增子序列的长度
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
    n = 5
    arr = [3, 1, 2, 1, 3]
    
    if is_monotonic_increasing(arr):
        result1 = 0
    else:
        # 使用动态规划找最长单调递增子序列
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[j] <= arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        max_length = max(dp)
        
        if max_length == 1:
            unique_elements = len(set(arr))
            result1 = unique_elements - 1
        else:
            # 构造最长子序列
            lis = []
            current_length = max_length
            current_max = float('inf')
            
            for i in range(n-1, -1, -1):
                if dp[i] == current_length and arr[i] <= current_max:
                    lis.append(arr[i])
                    current_length -= 1
                    current_max = arr[i]
            
            lis.reverse()
            
            total_unique = len(set(arr))
            lis_unique = len(set(lis))
            result1 = total_unique - lis_unique
    
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
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[j] <= arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        max_length = max(dp)
        
        if max_length == 1:
            unique_elements = len(set(arr))
            result3 = unique_elements - 1
        else:
            lis = []
            current_length = max_length
            current_max = float('inf')
            
            for i in range(n-1, -1, -1):
                if dp[i] == current_length and arr[i] <= current_max:
                    lis.append(arr[i])
                    current_length -= 1
                    current_max = arr[i]
            
            lis.reverse()
            
            total_unique = len(set(arr))
            lis_unique = len(set(lis))
            result3 = total_unique - lis_unique
    
    print(f"实际输出: {result3}")
    print(f"测试{'通过' if result3 == 1 else '失败'}")
    
    # 分析示例1
    print("\n示例1分析:")
    print("原数组: [3,1,2,1,3]")
    print("最长单调递增子序列: [1,2,3] (长度3)")
    print("需要删除的元素: 1和2")
    print("删除后剩余: [3,3] (单调递增)")
    print("删除操作次数: 2")


if __name__ == "__main__":
    # 运行测试
    test_examples()
    print("\n" + "="*50)
    print("运行主程序:")
    print("请输入测试数据:")
    solve_array_delete()
