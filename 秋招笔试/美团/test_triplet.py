from triplet_count import count_triplets, count_triplets_optimized, count_triplets_correct

def test_examples():
    """测试题目给出的示例"""
    print("测试示例1:")
    arr1 = [1, 5, 4, 2, 3]
    result1 = count_triplets_correct(arr1)
    print(f"输入: {arr1}")
    print(f"输出: {result1}")
    print(f"期望: 2")
    print()
    
    print("测试示例2:")
    arr2 = [20, -6, -9, -90, -73, 89, -90, 2, 19, 52, -16, -41, -22, 85, 24, -22, 66, 75, 78, 48, -36]
    result2 = count_triplets_correct(arr2)
    print(f"输入: {arr2}")
    print(f"输出: {result2}")
    print(f"期望: 134")
    print()

def test_simple_cases():
    """测试简单情况"""
    print("测试简单情况:")
    
    # 测试1：数组{4,1,2,3}
    arr1 = [4, 1, 2, 3]
    result1 = count_triplets_correct(arr1)
    print(f"数组{arr1}: {result1}")
    
    # 测试2：小数组
    arr2 = [3, 1, 2]
    result2 = count_triplets_correct(arr2)
    print(f"数组{arr2}: {result2}")
    
    # 测试3：全相同元素
    arr3 = [1, 1, 1, 1]
    result3 = count_triplets_correct(arr3)
    print(f"数组{arr3}: {result3}")

def test_edge_cases():
    """测试边界情况"""
    print("测试边界情况:")
    
    # 测试1：最小数组
    arr1 = [1, 2, 3]
    result1 = count_triplets_correct(arr1)
    print(f"最小数组{arr1}: {result1}")
    
    # 测试2：递减数组
    arr2 = [3, 2, 1]
    result2 = count_triplets_correct(arr2)
    print(f"递减数组{arr2}: {result2}")
    
    # 测试3：递增数组
    arr3 = [1, 2, 3, 4]
    result3 = count_triplets_correct(arr3)
    print(f"递增数组{arr3}: {result3}")

if __name__ == "__main__":
    test_examples()
    test_simple_cases()
    test_edge_cases()
