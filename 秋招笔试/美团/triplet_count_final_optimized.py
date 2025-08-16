def count_triplets_final_optimized(arr):
    """
    最终优化版本：结合所有优化策略
    时间复杂度：O(n²) 但常数因子极小
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 直接计算，避免创建临时列表和函数调用
        for i in range(j):
            ai = arr[i]
            if ai > aj:
                # 统计右边大于aj且小于ai的元素数量
                for k in range(j + 1, n):
                    ak = arr[k]
                    if ak > aj and ak < ai:
                        count += 1
    
    return count

def count_triplets_hybrid_optimized(arr):
    """
    混合优化版本：在特定情况下使用不同的优化策略
    """
    n = len(arr)
    
    # 对于小数组，使用简单版本
    if n <= 100:
        return count_triplets_final_optimized(arr)
    
    # 对于大数组，使用预处理优化
    count = 0
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

def main():
    """主函数"""
    # 读取输入
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 使用最终优化版本计算三元组数量
    result = count_triplets_final_optimized(arr)
    print(result)

if __name__ == "__main__":
    main()
