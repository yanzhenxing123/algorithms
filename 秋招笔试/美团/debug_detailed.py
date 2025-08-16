def debug_detailed_analysis():
    """详细分析每个三元组，找出问题所在"""
    
    # 测试示例1
    print("=== 详细分析示例1 ===")
    arr = [1, 5, 4, 2, 3]
    print(f"数组: {arr}")
    print(f"索引: {list(range(len(arr)))}")
    print()
    
    all_triplets = []
    valid_triplets = []
    
    # 生成所有可能的三元组 (i,j,k) 其中 1 ≤ i < j < k ≤ n
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                all_triplets.append((i, j, k))
                
                # 检查条件：ai > ak > aj
                ai, aj, ak = arr[i], arr[j], arr[k]
                condition = ai > ak > aj
                
                if condition:
                    valid_triplets.append((i, j, k))
                    print(f"三元组({i},{j},{k}): a{i}={ai}, a{j}={aj}, a{k}={ak} → {ai} > {ak} > {aj} ✓")
                else:
                    print(f"三元组({i},{j},{k}): a{i}={ai}, a{j}={aj}, a{k}={ak} → {ai} > {ak} > {aj} ✗")
    
    print(f"\n所有可能的三元组数量: {len(all_triplets)}")
    print(f"满足条件的三元组数量: {len(valid_triplets)}")
    print(f"满足条件的三元组: {valid_triplets}")
    
    # 检查题目示例中提到的三元组
    print(f"\n题目示例中提到的三元组:")
    mentioned = [(0, 1, 2), (0, 1, 3), (0, 2, 3)]  # (1,2,3), (1,2,4), (1,3,4) 转换为0索引
    for triplet in mentioned:
        i, j, k = triplet
        ai, aj, ak = arr[i], arr[j], arr[k]
        condition = ai > ak > aj
        print(f"({i+1},{j+1},{k+1}): a{i+1}={ai}, a{j+1}={aj}, a{k+1}={ak} → {ai} > {ak} > {aj} {'✓' if condition else '✗'}")

if __name__ == "__main__":
    debug_detailed_analysis()
