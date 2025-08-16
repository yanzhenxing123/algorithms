import time
from triplet_count_final import count_triplets_final
from triplet_count_optimized import count_triplets_optimized, count_triplets_fast, count_triplets_best

def test_performance():
    """测试不同版本算法的性能"""
    print("=== 性能测试 ===")
    
    # 测试用例
    test_cases = [
        # 小数组
        ([1, 5, 4, 2, 3], "示例1"),
        # 中等数组
        ([4, 1, 2, 3, 5, 6, 7, 8, 9, 10], "中等数组"),
        # 大数组（模拟超时情况）
        (list(range(100, 0, -1)) + list(range(1, 101)), "大数组"),  # 200个元素
    ]
    
    algorithms = [
        ("原始版本", count_triplets_final),
        ("优化版本", count_triplets_optimized),
        ("快速版本", count_triplets_fast),
        ("最佳版本", count_triplets_best),
    ]
    
    for arr, name in test_cases:
        print(f"\n测试用例: {name}")
        print(f"数组长度: {len(arr)}")
        
        for algo_name, algo_func in algorithms:
            try:
                start_time = time.time()
                result = algo_func(arr)
                end_time = time.time()
                
                execution_time = (end_time - start_time) * 1000  # 转换为毫秒
                print(f"  {algo_name}: 结果={result}, 时间={execution_time:.2f}ms")
                
            except Exception as e:
                print(f"  {algo_name}: 错误 - {e}")
        
        # 只测试小数组的正确性
        if len(arr) <= 10:
            print(f"  正确结果验证: {count_triplets_final(arr)}")

def test_correctness():
    """测试优化版本的正确性"""
    print("\n=== 正确性测试 ===")
    
    # 测试用例
    test_cases = [
        ([1, 5, 4, 2, 3], 2, "示例1"),
        ([4, 1, 2, 3], 3, "题目示例"),
    ]
    
    algorithms = [
        ("原始版本", count_triplets_final),
        ("优化版本", count_triplets_optimized),
        ("快速版本", count_triplets_fast),
        ("最佳版本", count_triplets_best),
    ]
    
    for arr, expected, name in test_cases:
        print(f"\n测试用例: {name}")
        print(f"数组: {arr}")
        print(f"期望: {expected}")
        
        for algo_name, algo_func in algorithms:
            try:
                result = algo_func(arr)
                status = "✓" if result == expected else "✗"
                print(f"  {algo_name}: {result} {status}")
            except Exception as e:
                print(f"  {algo_name}: 错误 - {e}")

if __name__ == "__main__":
    test_correctness()
    test_performance()
