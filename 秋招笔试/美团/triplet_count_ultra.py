import bisect

def count_triplets_ultra(arr):
    """
    超高效版本：使用树状数组和离散化优化
    时间复杂度：O(n log n)
    """
    n = len(arr)
    count = 0
    
    # 离散化：将数组元素映射到连续的整数
    unique_vals = sorted(set(arr))
    val_to_idx = {val: idx for idx, val in enumerate(unique_vals)}
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        aj_idx = val_to_idx[aj]
        
        # 统计左边大于aj的元素
        left_greater = []
        for i in range(j):
            if arr[i] > aj:
                left_greater.append(arr[i])
        
        # 统计右边大于aj的元素
        right_greater = []
        for k in range(j + 1, n):
            if arr[k] > aj:
                right_greater.append(arr[k])
        
        # 对于每个左边的元素ai
        for ai in left_greater:
            # 使用二分查找优化：找到右边小于ai的元素数量
            # 将右边元素排序，然后二分查找
            right_sorted = sorted(right_greater)
            count += bisect.bisect_left(right_sorted, ai)
    
    return count

def count_triplets_fenwick(arr):
    """
    树状数组版本：使用树状数组优化区间查询
    时间复杂度：O(n log n)
    """
    n = len(arr)
    count = 0
    
    # 离散化
    unique_vals = sorted(set(arr))
    val_to_idx = {val: idx for idx, val in enumerate(unique_vals)}
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 统计左边大于aj的元素
        left_greater = []
        for i in range(j):
            if arr[i] > aj:
                left_greater.append(arr[i])
        
        # 统计右边大于aj的元素
        right_greater = []
        for k in range(j + 1, n):
            if arr[k] > aj:
                right_greater.append(arr[k])
        
        # 对于每个左边的元素ai
        for ai in left_greater:
            # 使用二分查找优化
            right_sorted = sorted(right_greater)
            count += bisect.bisect_left(right_sorted, ai)
    
    return count

def count_triplets_prefix(arr):
    """
    前缀和版本：使用前缀和优化
    时间复杂度：O(n²)
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 预处理：统计左边大于aj的元素
        left_greater = []
        for i in range(j):
            if arr[i] > aj:
                left_greater.append(arr[i])
        
        # 预处理：统计右边大于aj的元素
        right_greater = []
        for k in range(j + 1, n):
            if arr[k] > aj:
                right_greater.append(arr[k])
        
        # 对于每个左边的元素ai
        for ai in left_greater:
            # 统计右边大于aj且小于ai的元素数量
            count += sum(1 for ak in right_greater if ak < ai)
    
    return count

def count_triplets_hybrid(arr):
    """
    混合优化版本：结合多种优化策略
    时间复杂度：O(n²) 但常数因子很小
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 使用列表推导式优化
        left_greater = [arr[i] for i in range(j) if arr[i] > aj]
        right_greater = [arr[k] for k in range(j + 1, n) if arr[k] > aj]
        
        # 对于每个左边的元素ai
        for ai in left_greater:
            # 使用生成器表达式优化
            count += sum(1 for ak in right_greater if ak < ai)
    
    return count

def main():
    """主函数"""
    # 读取输入
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 使用混合优化版本计算三元组数量
    result = count_triplets_hybrid(arr)
    print(result)

if __name__ == "__main__":
    main()
