"""
@Time: 2025/8/17 19:26
@Author: yanzx
@Description:

2
5 2
1 2 4 7 9
4 0
1 1 2 5

1
5 2
1 2 4 7 9
"""

import sys


import sys

def max_retained_elements(n, d, arr):
    """
    解决冲突约束问题的正确算法
    
    题目要求：
    1. 一次操作可以选择一对元素，并将其同时从数组中删除（数组长度减少2）
    2. 经过若干操作后，需要保证数组中不含任何"观点相近"的元素
    3. 目标是最大化保留的元素数量
    
    解题思路：
    1. 对数组排序
    2. 贪心策略：从左到右遍历，如果相邻元素差值 <= d，则删除这对元素
    3. 继续遍历剩余元素
    4. 最终剩余的元素数量就是答案
    
    时间复杂度：O(n log n) - 排序 + O(n) 遍历
    空间复杂度：O(1)
    
    Args:
        n: 数组长度
        d: 阈值
        arr: 数组
    
    Returns:
        最大保留元素数量
    """
    if n == 0:
        return 0
    
    # 对数组排序
    arr = sorted(arr)
    
    # 贪心策略：从左到右遍历，删除"观点相近"的元素对
    i = 0
    deleted_pairs = 0
    
    while i < n - 1:
        # 如果当前元素和下一个元素差值 <= d，删除这对元素
        if arr[i + 1] - arr[i] <= d:
            deleted_pairs += 1  # 记录删除的对数
            i += 2  # 跳过这对元素
        else:
            i += 1  # 继续检查下一个元素
    
    # 最终保留的元素数量 = 总数量 - 删除的对数 * 2
    return n - deleted_pairs * 2


def test_examples():
    """测试样例"""
    print("=== 测试样例 ===")
    
    # 测试用例1: n=5, d=2, arr=[1,2,4,7,9]
    print("测试用例1:")
    print("n=5, d=2, arr=[1,2,4,7,9]")
    arr1 = [1, 2, 4, 7, 9]
    arr1.sort()
    print(f"排序后: {arr1}")
    
    # 分析过程
    print("分析过程:")
    print("|1-2| = 1 ≤ 2, 删除1,2，剩余[4,7,9]")
    print("|4-7| = 3 > 2, 保留4")
    print("|7-9| = 2 ≤ 2, 删除7,9")
    print("最终保留: [4]")
    
    result1 = max_retained_elements(5, 2, [1, 2, 4, 7, 9])
    print(f"结果: {result1}")
    print()
    
    # 测试用例2: n=4, d=0, arr=[1,1,2,5]
    print("测试用例2:")
    print("n=4, d=0, arr=[1,1,2,5]")
    arr2 = [1, 1, 2, 5]
    arr2.sort()
    print(f"排序后: {arr2}")
    
    # 分析过程
    print("分析过程:")
    print("|1-1| = 0 ≤ 0, 删除1,1，剩余[2,5]")
    print("|2-5| = 3 > 0, 保留2,5")
    print("最终保留: [2,5]")
    
    result2 = max_retained_elements(4, 0, [1, 1, 2, 5])
    print(f"结果: {result2}")
    print()
    
    # 额外测试用例
    print("额外测试用例:")
    print("n=6, d=1, arr=[1,2,3,4,5,6]")
    result3 = max_retained_elements(6, 1, [1, 2, 3, 4, 5, 6])
    print(f"结果: {result3}")
    print()
    
    print("n=4, d=2, arr=[1,3,5,7]")
    result4 = max_retained_elements(4, 2, [1, 3, 5, 7])
    print(f"结果: {result4}")


def solve_conflict_constraints():
    """
    解决冲突约束问题
    
    思路：
    1. 对数组排序
    2. 贪心策略：从左到右遍历，如果相邻元素差值 <= d，则删除这对元素
    3. 继续遍历剩余元素
    4. 最终剩余的元素数量就是答案
    
    时间复杂度：O(n log n) - 排序 + O(n) 遍历
    空间复杂度：O(1)
    """
    
    # 读取输入
    T = int(input())  # 测试用例数量
    
    for _ in range(T):
        n, d = map(int, input().split())  # 数组长度和阈值
        arr = list(map(int, input().split()))  # 数组元素
        
        # 计算并输出结果
        result = max_retained_elements(n, d, arr)
        print(result)


if __name__ == "__main__":
    # 运行测试用例
    test_examples()
    
    print("\n=== 运行主程序 ===")
    print("请输入测试用例数量T，然后输入每组测试数据：")
    solve_conflict_constraints()