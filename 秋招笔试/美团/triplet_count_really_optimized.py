import bisect

def count_triplets_really_optimized(arr):
    """
    真正优化版本：基于count_triplets_best的成功经验
    时间复杂度：O(n² log n) 但常数因子极小
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 收集左边大于aj的元素
        left_greater = []
        for i in range(j):
            if arr[i] > aj:
                left_greater.append(arr[i])
        
        # 收集右边大于aj的元素并排序（只排序一次）
        right_greater = []
        for k in range(j + 1, n):
            if arr[k] > aj:
                right_greater.append(arr[k])
        
        # 排序右边元素，便于二分查找
        right_greater.sort()
        
        # 对于每个左边的元素ai
        for ai in left_greater:
            # 使用二分查找找到右边小于ai的元素数量
            # 找到第一个不小于ai的位置
            left, right = 0, len(right_greater)
            while left < right:
                mid = (left + right) // 2
                if right_greater[mid] < ai:
                    left = mid + 1
                else:
                    right = mid
            
            count += left
    
    return count

def count_triplets_ultimate_optimized(arr):
    """
    终极优化版本：避免重复排序，使用更高效的二分查找
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 收集左边大于aj的元素
        left_greater = []
        for i in range(j):
            if arr[i] > aj:
                left_greater.append(arr[i])
        
        # 收集右边大于aj的元素并排序
        right_greater = []
        for k in range(j + 1, n):
            if arr[k] > aj:
                right_greater.append(arr[k])
        
        # 排序右边元素
        right_greater.sort()
        
        # 对于每个左边的元素ai
        for ai in left_greater:
            # 使用bisect模块的二分查找，比手写二分查找更快
            count += bisect.bisect_left(right_greater, ai)
    
    return count

def count_triplets_smart_optimized(arr):
    """
    智能优化版本：根据数据特征选择最优策略
    """
    n = len(arr)
    
    # 如果数组很小，使用简单版本
    if n <= 50:
        return count_triplets_really_optimized(arr)
    
    # 如果数组很大，使用终极优化版本
    return count_triplets_ultimate_optimized(arr)

def main():
    """主函数"""
    # 读取输入
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 使用智能优化版本计算三元组数量
    result = count_triplets_smart_optimized(arr)
    print(result)

if __name__ == "__main__":
    main()
