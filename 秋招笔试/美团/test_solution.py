from array_bit_optimization import solve_case

def test_examples():
    """测试题目给出的示例"""
    print("测试示例1:")
    n1, arr1 = 3, [1, 2, 3]
    result1 = solve_case(n1, arr1)
    print(f"输入: n={n1}, arr={arr1}")
    print(f"输出: {result1}")
    print(f"期望: (6, 0)")
    print()
    
    print("测试示例2:")
    n2, arr2 = 2, [33, 3]
    result2 = solve_case(n2, arr2)
    print(f"输入: n={n2}, arr={arr2}")
    print(f"输出: {result2}")
    print(f"期望: (36, 3)")
    print()
    
    print("测试示例3:")
    n3, arr3 = 3, [2, 3, 123]
    result3 = solve_case(n3, arr3)
    print(f"输入: n={n3}, arr={arr3}")
    print(f"输出: {result3}")
    print(f"期望: (93, 3)")
    print()

def test_edge_cases():
    """测试边界情况"""
    print("测试边界情况:")
    
    # 全为0的数组
    n1, arr1 = 3, [0, 0, 0]
    result1 = solve_case(n1, arr1)
    print(f"全0数组: {result1}")
    
    # 单个元素
    n2, arr2 = 1, [5]
    result2 = solve_case(n2, arr2)
    print(f"单个元素: {result2}")
    
    # 大数
    n3, arr3 = 2, [1000000, 999999]
    result3 = solve_case(n3, arr3)
    print(f"大数: {result3}")

if __name__ == "__main__":
    test_examples()
    test_edge_cases()
