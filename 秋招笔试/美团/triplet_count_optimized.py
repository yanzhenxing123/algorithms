def count_triplets_optimized(arr):
    """
    优化版本：计算满足条件的三元组数量
    条件：1 ≤ i < j < k ≤ n 且 ai > ak > aj
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
            for ak in right_greater:
                if ak < ai:
                    count += 1
    
    return count

def count_triplets_fast(arr):
    """
    快速版本：使用更高效的数据结构
    时间复杂度：O(n² log n)
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
            # 统计右边大于aj且小于ai的元素数量
            count += sum(1 for ak in right_greater if ak < ai)
    
    return count

def count_triplets_best(arr):
    """
    最佳版本：使用排序和二分查找优化
    时间复杂度：O(n² log n)
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

def main():
    """主函数"""
    # 读取输入
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 使用最佳版本计算三元组数量
    result = count_triplets_best(arr)
    print(result)

if __name__ == "__main__":
    main()
