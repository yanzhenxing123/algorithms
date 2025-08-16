def debug_triplets(arr):
    """调试函数：手动验证三元组计算"""
    n = len(arr)
    print(f"数组: {arr}")
    print(f"长度: {n}")
    print()
    
    count = 0
    triplets = []
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        print(f"j={j}, aj={aj}")
        
        # 找到左边大于aj的元素（作为ai的候选）
        for i in range(j):
            ai = arr[i]
            if ai > aj:
                print(f"  左边 i={i}, ai={ai} > aj={aj}")
                
                # 找到右边大于aj且小于ai的元素（作为ak的候选）
                for k in range(j + 1, n):
                    ak = arr[k]
                    if ak > aj and ak < ai:
                        print(f"    右边 k={k}, ak={ak} (满足 {aj} < {ak} < {ai})")
                        count += 1
                        triplets.append((i, j, k))
        
        print()
    
    print(f"总的三元组数量: {count}")
    print(f"具体三元组: {triplets}")
    return count

# 测试示例1
print("=== 测试示例1 ===")
arr1 = [1, 5, 4, 2, 3]
result1 = debug_triplets(arr1)
print(f"期望: 2, 实际: {result1}")
print()

# 测试示例2的前几个元素
print("=== 测试示例2（前10个元素）===")
arr2 = [20, -6, -9, -90, -73, 89, -90, 2, 19, 52]
result2 = debug_triplets(arr2)
print(f"前10个元素的结果: {result2}")
