def debug_full_example2():
    """详细调试完整的示例2"""
    print("详细调试完整的示例2:")
    
    # 完整的示例2数组
    arr = [20, -6, -9, -90, -73, 89, -90, 2, 19, 52, -16, -41, -22, 85, 24, -22, 66, 75, 78, 48, -36]
    
    print(f"数组长度: {len(arr)}")
    print(f"数组: {arr}")
    print()
    
    count = 0
    triplets = []
    
    # 对于每个位置j
    for j in range(1, len(arr) - 1):
        aj = arr[j]
        print(f"j={j}, aj={aj}")
        
        # 找到左边大于aj的元素（作为ai的候选）
        for i in range(j):
            ai = arr[i]
            if ai > aj:
                print(f"  左边 i={i}, ai={ai} > aj={aj}")
                
                # 找到右边大于aj且小于ai的元素（作为ak的候选）
                for k in range(j + 1, len(arr)):
                    ak = arr[k]
                    if ak > aj and ak < ai:
                        print(f"    右边 k={k}, ak={ak} (满足 {aj} < {ak} < {ai})")
                        count += 1
                        triplets.append((i, j, k))
        
        print()
    
    print(f"总的三元组数量: {count}")
    print(f"具体三元组数量: {len(triplets)}")
    
    # 显示前20个三元组
    print(f"前20个三元组: {triplets[:20]}")
    
    # 按j分组统计
    j_counts = {}
    for i, j, k in triplets:
        if j not in j_counts:
            j_counts[j] = 0
        j_counts[j] += 1
    
    print(f"按j分组的统计: {j_counts}")
    
    return count

if __name__ == "__main__":
    debug_full_example2()
