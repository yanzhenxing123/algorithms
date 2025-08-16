def count_triplets_final(arr):
    """
    最终版本：计算满足条件的三元组数量
    条件：1 ≤ i < j < k ≤ n 且 ai > ak > aj
    
    Args:
        arr: 整数数组
    
    Returns:
        满足条件的三元组数量
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j (1 ≤ j ≤ n-2)
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 找到左边大于aj的元素（作为ai的候选）
        for i in range(j):
            ai = arr[i]
            if ai > aj:  # ai > aj
                # 找到右边大于aj且小于ai的元素（作为ak的候选）
                for k in range(j + 1, n):
                    ak = arr[k]
                    if ak > aj and ak < ai:  # ak > aj 且 ak < ai
                        count += 1
    
    return count

def verify_example():
    """验证题目给出的示例"""
    print("验证题目示例:")
    
    # 示例：数组{4,1,2,3}
    arr = [4, 1, 2, 3]
    print(f"数组: {arr}")
    
    # 手动验证每个三元组
    triplets = []
    n = len(arr)
    
    for j in range(1, n - 1):
        aj = arr[j]
        for i in range(j):
            ai = arr[i]
            if ai > aj:
                for k in range(j + 1, n):
                    ak = arr[k]
                    if ak > aj and ak < ai:
                        triplets.append((i+1, j+1, k+1))  # 转换为1索引
                        print(f"三元组({i+1},{j+1},{k+1}): a{i+1}={ai}, a{j+1}={aj}, a{k+1}={ak} → {ai} > {ak} > {aj} ✓")
    
    print(f"满足条件的三元组: {triplets}")
    print(f"数量: {len(triplets)}")
    print()

def main():
    """主函数"""
    # 读取输入
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 计算三元组数量
    result = count_triplets_final(arr)
    print(result)

if __name__ == "__main__":
    main()
