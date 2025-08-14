"""
@Time: 2024/3/22 22:47
@Author: yanzx
@Desc: 128. 最长连续序列

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

算法思路详解：
方法一：哈希表记录端点长度（Union-Find思想）
- 对每个新数字，查看其左右邻居的连续长度
- 更新新形成序列的两个端点的长度值
- 时间复杂度：O(n)，空间复杂度：O(n)

方法二：集合查找（最优解）
- 将所有数字放入集合，便于O(1)查找
- 对每个数字，只有当它是序列起点时才开始计数
- 如何判断起点：num-1不在集合中
- 时间复杂度：O(n)，空间复杂度：O(n)
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        方法一：哈希表记录端点长度（Union-Find思想）
        
        核心思想：
        1. 对于每个新加入的数字num，查看其左邻居(num-1)和右邻居(num+1)的连续长度
        2. 计算新形成序列的总长度：left_len + 1 + right_len
        3. 只需要更新新序列两个端点的长度值，中间的值不重要
        4. 左端点位置：num - left_len，右端点位置：num + right_len
        
        为什么只更新端点？
        - 后续遍历时，只有端点的邻居才可能被访问到
        - 中间节点的值不会影响后续计算
        
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        if not nums:
            return 0
            
        max_length = 0
        hash_dict = {}  # 存储每个数字对应的连续序列长度
        
        for num in nums:
            # 跳过重复数字
            if num in hash_dict:
                continue
            
            # 获取左邻居的连续长度（如果不存在则为0）
            left_len = hash_dict.get(num - 1, 0)
            # 获取右邻居的连续长度（如果不存在则为0）
            right_len = hash_dict.get(num + 1, 0)
            
            # 计算包含当前数字的连续序列长度
            cur_len = left_len + 1 + right_len
            
            # 更新最大长度
            max_length = max(max_length, cur_len)
            
            # 将当前数字标记为已访问（值可以是任意非0值）
            hash_dict[num] = cur_len
            
            # 关键步骤：更新新形成序列的两个端点的长度值
            # 左端点：num - left_len
            hash_dict[num - left_len] = cur_len
            # 右端点：num + right_len  
            hash_dict[num + right_len] = cur_len
            
        return max_length

    def longestConsecutive_optimal(self, nums: List[int]) -> int:
        """
        方法二：集合查找法（最优解）
        
        核心思想：
        1. 将所有数字放入集合，实现O(1)查找
        2. 遍历集合中的每个数字
        3. 只有当num-1不在集合中时，num才是序列的起点
        4. 从起点开始，连续查找num+1, num+2, ...直到不存在
        5. 记录每个序列的长度，取最大值
        
        为什么效率高？
        - 每个数字最多被访问2次：一次判断是否为起点，一次作为序列中的元素
        - 避免了重复计算中间序列的长度
        
        时间复杂度：O(n)，空间复杂度：O(n)
        """
        if not nums:
            return 0
            
        num_set = set(nums)  # 去重并支持O(1)查找
        longest_streak = 0
        
        for num in num_set:
            # 只有当num-1不在集合中时，num才是序列的起点
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # 从起点开始，连续查找后续数字
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # 更新最长序列长度
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak

    def longestConsecutive3(self, nums: List[int]) -> int:
        """
        方法一的另一种实现（保留原有代码供对比学习）
        """
        if not nums or len(nums) == 1:
            return len(nums)
        hash_dict = {}
        max_len = 0
        for num in nums:
            if num in hash_dict:
                continue
            left = hash_dict.get(num - 1, 0)
            right = hash_dict.get(num + 1, 0)
            cur_len = 1 + left + right
            max_len = max(max_len, cur_len)
            # 更新端点值
            hash_dict[num] = cur_len
            hash_dict[num + right] = cur_len
            hash_dict[num - left] = cur_len
        return max_len

    def longestConsecutive2(self, nums: List[int]) -> int:
        """
        官方题目给的最优解（保留原有代码供对比学习）
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:  # num-1没在num_set中说明此数字是序列中的第一个
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak


def test_longest_consecutive():
    """
    测试最长连续序列算法的各种情况
    """
    solution = Solution()
    
    # 测试用例1：基本测试用例
    nums1 = [100, 4, 200, 1, 3, 2]
    expected1 = 4  # [1, 2, 3, 4]
    result1_method1 = solution.longestConsecutive(nums1)
    result1_method2 = solution.longestConsecutive_optimal(nums1)
    print(f"测试用例1: {nums1}")
    print(f"期望结果: {expected1}")
    print(f"方法一结果: {result1_method1}")
    print(f"方法二结果: {result1_method2}")
    print(f"测试通过: {result1_method1 == expected1 and result1_method2 == expected1}")
    print("-" * 50)
    
    # 测试用例2：全连续测试
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    expected2 = 9  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
    result2_method1 = solution.longestConsecutive(nums2)
    result2_method2 = solution.longestConsecutive_optimal(nums2)
    print(f"测试用例2: {nums2}")
    print(f"期望结果: {expected2}")
    print(f"方法一结果: {result2_method1}")
    print(f"方法二结果: {result2_method2}")
    print(f"测试通过: {result2_method1 == expected2 and result2_method2 == expected2}")
    print("-" * 50)
    
    # 测试用例3：边界情况 - 空数组
    nums3 = []
    expected3 = 0
    result3_method1 = solution.longestConsecutive(nums3)
    result3_method2 = solution.longestConsecutive_optimal(nums3)
    print(f"测试用例3: {nums3}")
    print(f"期望结果: {expected3}")
    print(f"方法一结果: {result3_method1}")
    print(f"方法二结果: {result3_method2}")
    print(f"测试通过: {result3_method1 == expected3 and result3_method2 == expected3}")
    print("-" * 50)
    
    # 测试用例4：单元素
    nums4 = [1]
    expected4 = 1
    result4_method1 = solution.longestConsecutive(nums4)
    result4_method2 = solution.longestConsecutive_optimal(nums4)
    print(f"测试用例4: {nums4}")
    print(f"期望结果: {expected4}")
    print(f"方法一结果: {result4_method1}")
    print(f"方法二结果: {result4_method2}")
    print(f"测试通过: {result4_method1 == expected4 and result4_method2 == expected4}")
    print("-" * 50)
    
    # 测试用例5：重复元素
    nums5 = [1, 2, 0, 1]
    expected5 = 3  # [0, 1, 2]
    result5_method1 = solution.longestConsecutive(nums5)
    result5_method2 = solution.longestConsecutive_optimal(nums5)
    print(f"测试用例5: {nums5}")
    print(f"期望结果: {expected5}")
    print(f"方法一结果: {result5_method1}")
    print(f"方法二结果: {result5_method2}")
    print(f"测试通过: {result5_method1 == expected5 and result5_method2 == expected5}")
    print("-" * 50)
    
    # 测试用例6：负数测试
    nums6 = [-1, -2, -3, 1, 2, 3]
    expected6 = 3  # [-3, -2, -1] 或 [1, 2, 3]
    result6_method1 = solution.longestConsecutive(nums6)
    result6_method2 = solution.longestConsecutive_optimal(nums6)
    print(f"测试用例6: {nums6}")
    print(f"期望结果: {expected6}")
    print(f"方法一结果: {result6_method1}")
    print(f"方法二结果: {result6_method2}")
    print(f"测试通过: {result6_method1 == expected6 and result6_method2 == expected6}")
    print("-" * 50)


if __name__ == '__main__':
    print("=== 128. 最长连续序列 - 完整测试 ===")
    print()
    test_longest_consecutive()
    
    print("\n=== 算法复杂度分析 ===")
    print("方法一（哈希表记录端点长度）：")
    print("- 时间复杂度：O(n)，每个元素最多被访问常数次")
    print("- 空间复杂度：O(n)，哈希表存储")
    print("- 优点：思路直观，类似Union-Find的合并思想")
    print("- 缺点：需要维护端点信息，代码稍复杂")
    print()
    print("方法二（集合查找法）：")
    print("- 时间复杂度：O(n)，每个元素最多被访问2次")
    print("- 空间复杂度：O(n)，集合存储")
    print("- 优点：代码简洁，逻辑清晰，是最优解")
    print("- 缺点：需要理解'起点'的概念")
