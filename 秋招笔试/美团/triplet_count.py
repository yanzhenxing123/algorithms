def count_triplets(arr):
    """
    计算满足条件的三元组数量：ai > ak > aj 且 i < j < k
    
    Args:
        arr: 整数数组
    
    Returns:
        满足条件的三元组数量
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j，找到满足条件的三元组
    for j in range(1, n - 1):  # j从1开始，到n-2结束
        aj = arr[j]
        
        # 统计左边大于aj的元素数量
        left_greater = 0
        for i in range(j):
            if arr[i] > aj:
                left_greater += 1
        
        # 统计右边大于aj且小于左边某个元素的元素数量
        for i in range(j):
            if arr[i] > aj:  # ai > aj
                for k in range(j + 1, n):
                    if arr[k] > aj and arr[k] < arr[i]:  # ak > aj 且 ak < ai
                        count += 1
    
    return count

def count_triplets_optimized(arr):
    """
    优化版本：使用更高效的方法计算三元组数量
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 统计左边大于aj的元素
        left_greater = []
        for i in range(j):
            if arr[i] > aj:
                left_greater.append(arr[i])
        
        # 统计右边大于aj且小于左边某个元素的元素
        for ai in left_greater:
            for k in range(j + 1, n):
                if arr[k] > aj and arr[k] < ai:
                    count += 1
    
    return count

def count_triplets_correct(arr):
    """
    正确版本：确保满足条件 ai > ak > aj 且 i < j < k
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 找到左边大于aj的元素（作为ai的候选）
        for i in range(j):
            ai = arr[i]
            if ai > aj:
                # 找到右边大于aj且小于ai的元素（作为ak的候选）
                for k in range(j + 1, n):
                    ak = arr[k]
                    if ak > aj and ak < ai:
                        count += 1
    
    return count

def count_triplets_efficient(arr):
    """
    高效版本：使用更优化的算法
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 统计左边大于aj的元素
        left_greater = []
        for i in range(j):
            if arr[i] > aj:
                left_greater.append(arr[i])
        
        # 统计右边大于aj且小于左边某个元素的元素
        for ai in left_greater:
            for k in range(j + 1, n):
                if arr[k] > aj and arr[k] < ai:
                    count += 1
    
    return count

def main():
    """主函数"""
    # 读取输入
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 计算三元组数量
    result = count_triplets_correct(arr)
    print(result)

if __name__ == "__main__":
    main()
