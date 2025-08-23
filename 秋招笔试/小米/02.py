"""
@Author: yanzx
@Time: 2025/8/23 16:37 
@Description:


3
1 1
2
5 1
1 2 4 7 8
5 3
6 4 7 10 5

0
2
1
"""


def can_make_valid(h, k, x):
    """
    判断是否可以通过k次操作使得所有相邻高度差不超过x

    Args:
        h: 山的高度数组
        k: 可用的操作次数
        x: 登山鞋耐久度

    Returns:
        bool: 是否可行
    """
    n = len(h)
    if n <= 1:
        return True

    # 复制数组进行测试
    h_test = h.copy()
    operations_used = 0

    # 从左到右遍历
    for i in range(n - 1):
        current_diff = abs(h_test[i + 1] - h_test[i])

        if current_diff > x:
            if operations_used >= k:
                return False

            operations_used += 1

            # 贪心策略：修改下一座山，使其与当前山的高度差为x
            if h_test[i + 1] > h_test[i]:
                h_test[i + 1] = h_test[i] + x
            else:
                h_test[i + 1] = h_test[i] - x

    return operations_used <= k


def solve_hiking_shoes(n, k, h):
    """
    解决登山鞋问题

    Args:
        n: 山的数量
        k: 可用的操作次数
        h: 山的高度数组

    Returns:
        int: 登山鞋的最低耐久度
    """
    if n <= 1:
        return 0

    # 如果k >= n-1，可以修改所有山使它们高度相等
    if k >= n - 1:
        return 0

    # 计算初始的最大高度差
    max_diff = max(abs(h[i] - h[i - 1]) for i in range(1, n)) if n > 1 else 0

    # 二分查找耐久度x
    left = 0
    right = max_diff

    while left < right:
        mid = (left + right) // 2

        if can_make_valid(h, k, mid):
            right = mid
        else:
            left = mid + 1

    return left


def main():
    """主函数"""
    # 读取测试用例数量
    T = int(input())

    # 处理每个测试用例
    for _ in range(T):
        # 读取n和k
        n, k = map(int, input().split())

        # 读取山的高度
        h = list(map(int, input().split()))

        # 计算结果
        result = solve_hiking_shoes(n, k, h)

        # 输出结果
        print(result)


if __name__ == "__main__":
    main()
