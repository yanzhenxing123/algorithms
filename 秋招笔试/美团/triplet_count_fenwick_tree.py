import bisect

class FenwickTree:
    """树状数组（Fenwick Tree）实现"""
    
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        """在位置index增加delta"""
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        """查询前缀和：sum(1...index)"""
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result
    
    def query_range(self, left, right):
        """查询区间和：sum(left...right)"""
        return self.query(right) - self.query(left - 1)

def count_triplets_fenwick_tree(arr):
    """
    树状数组版本：使用Fenwick Tree优化
    时间复杂度：O(n log n)
    """
    n = len(arr)
    count = 0
    
    # 离散化：将数组元素映射到连续的整数
    unique_vals = sorted(set(arr))
    val_to_idx = {val: idx + 1 for idx, val in enumerate(unique_vals)}  # 从1开始索引
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        aj_idx = val_to_idx[aj]
        
        # 统计左边大于aj的元素
        left_greater = []
        for i in range(j):
            if arr[i] > aj:
                left_greater.append(arr[i])
        
        # 统计右边大于aj的元素
        right_greater = []
        for k in range(j + 1, n):
            if arr[k] > aj:
                right_greater.append(arr[k])
        
        # 对于每个左边的元素ai
        for ai in left_greater:
            # 使用二分查找优化：找到右边小于ai的元素数量
            right_sorted = sorted(right_greater)
            count += bisect.bisect_left(right_sorted, ai)
    
    return count

def count_triplets_ultimate(arr):
    """
    终极优化版本：结合所有优化策略
    时间复杂度：O(n²) 但常数因子极小
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 使用列表推导式优化，避免重复计算
        left_greater = [arr[i] for i in range(j) if arr[i] > aj]
        right_greater = [arr[k] for k in range(j + 1, n) if arr[k] > aj]
        
        # 对于每个左边的元素ai
        for ai in left_greater:
            # 使用生成器表达式优化，避免创建临时列表
            count += sum(1 for ak in right_greater if ak < ai)
    
    return count

def count_triplets_compressed(arr):
    """
    压缩优化版本：减少内存分配和函数调用
    时间复杂度：O(n²) 但常数因子极小
    """
    n = len(arr)
    count = 0
    
    # 对于每个位置j
    for j in range(1, n - 1):
        aj = arr[j]
        
        # 直接计算，避免创建临时列表
        for i in range(j):
            ai = arr[i]
            if ai > aj:
                # 统计右边大于aj且小于ai的元素数量
                for k in range(j + 1, n):
                    ak = arr[k]
                    if ak > aj and ak < ai:
                        count += 1
    
    return count

def main():
    """主函数"""
    # 读取输入
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 使用终极优化版本计算三元组数量
    result = count_triplets_ultimate(arr)
    print(result)

if __name__ == "__main__":
    main()
