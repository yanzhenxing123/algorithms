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
    
    # 贪心策略：从高位到低位尝试设置1
    best_x = 0
    best_sum = sum(arr)
    
    # 尝试在每一位上设置1
    for bit in range(max_bits):
        candidate_x = 1 << bit
        
        # 检查这个x是否能增加总和
        current_sum = 0
        current_x = candidate_x
        
        # 模拟操作过程
        temp_arr = arr.copy()
        
        # 贪心选择：优先操作能带来最大增益的元素
        gains = []
        for i in range(n):
            # 计算操作后的增益
            new_val = temp_arr[i] | current_x
            gain = new_val - temp_arr[i]
            gains.append((gain, i))
        
        # 按增益降序排序
        gains.sort(reverse=True)
        
        # 执行操作
        for gain, idx in gains:
            if gain > 0 and current_x > 0:
                temp_arr[idx] = temp_arr[idx] | current_x
                current_x = temp_arr[idx] & current_x
                if current_x == 0:
                    break
        
        current_sum = sum(temp_arr)
        
        # 更新最佳结果
        if current_sum > best_sum or (current_sum == best_sum and candidate_x < best_x):
            best_sum = current_sum
            best_x = candidate_x
    
    # 还需要检查更大的x值（在位数限制内）
    for bit1 in range(max_bits):
        for bit2 in range(bit1 + 1, max_bits):
            candidate_x = (1 << bit1) | (1 << bit2)
            
            current_sum = 0
            current_x = candidate_x
            temp_arr = arr.copy()
            
            # 贪心选择操作顺序
            gains = []
            for i in range(n):
                new_val = temp_arr[i] | current_x
                gain = new_val - temp_arr[i]
                gains.append((gain, i))
            
            gains.sort(reverse=True)
            
            for gain, idx in gains:
                if gain > 0 and current_x > 0:
                    temp_arr[idx] = temp_arr[idx] | current_x
                    current_x = temp_arr[idx] & current_x
                    if current_x == 0:
                        break
            
            current_sum = sum(temp_arr)
            
            if current_sum > best_sum or (current_sum == best_sum and candidate_x < best_x):
                best_sum = current_sum
                best_x = candidate_x
    
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
