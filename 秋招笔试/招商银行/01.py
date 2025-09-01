"""
@Author: yanzx
@Time: 2025/9/1 19:37 
@Description: 
"""

from collections import defaultdict

from typing import List


class SolutionOptimized:
    def largestValsFromLabels(self, values: List[int], labels: List[int], w: int, m: int) -> int:
        """
        优化版本：使用贪心+状态压缩
        """
        n = len(values)
        if n == 0 or w == 0:
            return 0

        # 创建(价值, 标签, 索引)的元组列表
        items = [(values[i], labels[i], i) for i in range(n)]

        # 按价值降序排序
        items.sort(reverse=True)

        # 记录每类已选择的数量
        label_count = {}
        selected_indices = set()
        total_value = 0
        selected_count = 0

        for value, label, idx in items:
            if selected_count >= w:
                break

            # 检查是否可以选择当前基金
            if self.can_select(idx, label, label_count, m, selected_indices):
                # 选择当前基金
                label_count[label] = label_count.get(label, 0) + 1
                selected_indices.add(idx)
                total_value += value
                selected_count += 1

        return total_value

    def can_select(self, idx: int, label: int, label_count: dict, m: int, selected_indices: set) -> bool:
        """检查是否可以选择当前基金"""
        # 检查类别数量约束
        if label_count.get(label, 0) >= m:
            return False

        # 检查非连续约束
        if idx - 1 in selected_indices or idx + 1 in selected_indices:
            return False

        return True


# 测试优化版本
def test_optimized_solution():
    """测试优化版本的Solution"""
    print("测试优化版本的Solution")
    print("=" * 50)

    values = [9, 8, 7, 6, 5]
    labels = [1, 1, 2, 2, 3]
    w, m = 3, 1

    solution = SolutionOptimized()
    result = solution.largestValsFromLabels(values, labels, w, m)
    print(f"基金价值: {values}")
    print(f"基金类别: {labels}")
    print(f"最多选择: {w}, 每类最多: {m}")
    print(f"最大价值: {result}")


if __name__ == "__main__":
    test_optimized_solution()