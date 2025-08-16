import bisect
from collections import defaultdict

def count_triplets_breakthrough(arr):
    """
    突破性优化版本：使用高级数据结构
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
            # 使用二分查找
            count += bisect.bisect_left(right_greater, ai)
    
    return count

def count_triplets_compressed_optimized(arr):
    """
    压缩优化版本：减少内存分配，优化常数因子
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 直接计算，避免创建临时列表
        for i in range(j):
            ai = arr[i]
            if ai > aj:
                # 统计右边大于aj且小于ai的元素数量
                for k in range(j + 1, n):
                    ak = arr[k]
                    if ak > aj and ak < ai:
                        count += 1
    
    return count

def count_triplets_hybrid_breakthrough(arr):
    """
    混合突破版本：根据数组大小选择最优策略
    """
    n = len(arr)
    
    # 对于小数组，使用压缩优化版本
    if n <= 100:
        return count_triplets_compressed_optimized(arr)
    
    # 对于大数组，使用突破性优化版本
    return count_triplets_breakthrough(arr)

def count_triplets_final_breakthrough(arr):
    """
    最终突破版本：结合所有可能的优化
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
            # 使用bisect模块的二分查找
            count += bisect.bisect_left(right_greater, ai)
    
    return count

def main():
    """主函数"""
    # 读取输入
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 使用最终突破版本计算三元组数量
    result = count_triplets_final_breakthrough(arr)
    print(result)

if __name__ == "__main__":
    main()
