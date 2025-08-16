from triplet_count import count_triplets_correct

def test_full_example2():
    """测试完整的示例2"""
    print("测试完整的示例2:")
    
    # 完整的示例2数组
    arr = [20, -6, -9, -90, -73, 89, -90, 2, 19, 52, -16, -41, -22, 85, 24, -22, 66, 75, 78, 48, -36]
    
    print(f"数组长度: {len(arr)}")
    print(f"数组: {arr}")
    print()
    
    # 计算三元组数量
    result = count_triplets_correct(arr)
    print(f"计算得到的三元组数量: {result}")
    print(f"期望的三元组数量: 134")
    print(f"是否匹配: {'✓' if result == 134 else '✗'}")
    
    # 如果结果不匹配，让我们分析一下可能的原因
    if result != 134:
        print("\n可能的原因分析:")
        print("1. 题目可能有其他约束条件")
        print("2. 题目可能有不同的理解方式")
        print("3. 期望值可能有误")
        print("4. 我们的算法可能有遗漏")

if __name__ == "__main__":
    test_full_example2()
