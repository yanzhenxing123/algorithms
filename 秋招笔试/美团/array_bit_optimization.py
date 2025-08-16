def get_binary_length(num):
    """获取数字的二进制位数，0的位数为1"""
    if num == 0:
        return 1
    return num.bit_length()

def solve_case(n, arr):
    """解决单个测试用例"""
    if n == 0:
        return 0, 0
    
    # 找到数组中的最大值，确定x的二进制位数上限
    max_val = max(arr)
    max_bits = get_binary_length(max_val)
    
    # 如果数组全为0，直接返回
    if max_val == 0:
        return 0, 0
    
    best_x = 0
    best_sum = sum(arr)
    
    # 尝试不同的初始x值
    # 从0开始，到不超过最大值的所有可能值
    for x in range(0, min(1 << max_bits, max_val + 1)):
        # 模拟操作过程
        temp_arr = arr.copy()
        current_x = x
        
        # 贪心策略：每次选择能带来最大增益的元素进行操作
        # 操作可以重复进行，直到x变为0或无法获得增益
        while current_x > 0:
            max_gain = 0
            best_idx = -1
            
            # 找到能带来最大增益的元素
            for i in range(n):
                new_val = temp_arr[i] | current_x
                gain = new_val - temp_arr[i]
                if gain > max_gain:
                    max_gain = gain
                    best_idx = i
            
            # 如果没有增益，退出
            if max_gain == 0:
                break
            
            # 执行操作
            temp_arr[best_idx] = temp_arr[best_idx] | current_x
            current_x = temp_arr[best_idx] & current_x
        
        current_sum = sum(temp_arr)
        
        # 更新最佳结果
        if current_sum > best_sum or (current_sum == best_sum and x < best_x):
            best_sum = current_sum
            best_x = x
    
    return best_sum, best_x

def main():
    """主函数"""
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        
        max_sum, min_x = solve_case(n, arr)
        print(f"{max_sum} {min_x}")

if __name__ == "__main__":
    main()
