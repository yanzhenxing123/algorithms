def solve_road_maintenance():
    """
    解决道路维修时间计算问题
    输入：T个测试用例，每个包含H（总时间）和N个预警时段
    输出：每个测试用例的可用维修时间
    """
    
    def merge_intervals(intervals):
        """
        合并重叠的区间
        输入：intervals - 区间列表，每个区间为 [start, end]
        输出：合并后的区间列表
        """
        if not intervals:
            return []
        
        # 按开始时间排序
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            # 如果当前区间与最后一个合并区间重叠，则合并
            if current[0] <= merged[-1][1] + 1:  # +1 因为时间点是连续的整数
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                merged.append(current)
        
        return merged
    
    def calculate_available_time(H, warning_periods):
        """
        计算可用的维修时间
        输入：H - 总时间，warning_periods - 预警时段列表
        输出：可用维修时间总数
        """
        if not warning_periods:
            return H
        
        # 合并重叠的预警时段
        merged_warnings = merge_intervals(warning_periods)
        
        # 计算被预警时段覆盖的总时间
        covered_time = 0
        for start, end in merged_warnings:
            covered_time += end - start + 1
        
        # 可用时间 = 总时间 - 被覆盖时间
        available_time = H - covered_time
        
        return max(0, available_time)
    
    # 读取输入
    T = int(input())  # 测试用例数量
    
    for _ in range(T):
        H = int(input())  # 总工作时间
        N = int(input())  # 预警时段数量
        
        warning_periods = []
        for _ in range(N):
            xi, yi = map(int, input().split())
            warning_periods.append([xi, yi])
        
        # 计算并输出结果
        result = calculate_available_time(H, warning_periods)
        print(result)


# 测试函数
def test_example():
    """
    测试示例用例
    """
    print("测试示例:")
    print("输入:")
    print("1")
    print("10")
    print("2")
    print("5 10")
    print("5 5")
    print()
    print("预期输出: 4")
    print()
    
    # 模拟输入
    H = 10
    warning_periods = [[5, 10], [5, 5]]
    
    def merge_intervals(intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for current in intervals[1:]:
            if current[0] <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                merged.append(current)
        return merged
    
    def calculate_available_time(H, warning_periods):
        if not warning_periods:
            return H
        merged_warnings = merge_intervals(warning_periods)
        covered_time = 0
        for start, end in merged_warnings:
            covered_time += end - start + 1
        available_time = H - covered_time
        return max(0, available_time)
    
    result = calculate_available_time(H, warning_periods)
    print(f"实际输出: {result}")
    print(f"测试{'通过' if result == 4 else '失败'}")


if __name__ == "__main__":
    # 运行测试
    test_example()
    print("\n" + "="*50)
    print("运行主程序:")
    print("请输入测试用例数据:")
    solve_road_maintenance()
