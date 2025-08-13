"""
@Author: yanzx
@Date: 2025/3/5 14:22
@Description:

其实就是 x_next = (x + S / x) / 2


"""


def sqrt_newton(S, tolerance=1e-7, max_iterations=1000):
    # 初始猜测值
    x = S / 2.0
    iteration = 0

    while iteration < max_iterations:
        # 计算下一个近似值
        x_new = 0.5 * (x + S / x)

        # 检查是否满足误差要求
        if abs(x_new - x) < tolerance:
            return x_new

        x = x_new
        iteration += 1

    return x  # 如果没有在最大迭代次数内收敛，返回当前结果



def binary_search_sqrt(n, tolerance=1e-6):
    """
    使用二分法计算一个数的平方根。

    :param n: 输入的数
    :param tolerance: 收敛的误差容忍度
    :return: n 的平方根
    """
    if n < 0:
        raise ValueError("不能计算负数的平方根")
    if n == 0:
        return 0
    # 确定二分查找的左右边界
    left = 0.0
    right = max(1.0, n)

    while (right - left) > tolerance:
        mid = (left + right) / 2
        mid_squared = mid * mid
        if mid_squared < n:
            left = mid
        else:
            right = mid
    return (left + right) / 2


# 示例：求平方根
S = 4
result = binary_search_sqrt(S)
print(f"The square root of {S} is approximately {result}")
