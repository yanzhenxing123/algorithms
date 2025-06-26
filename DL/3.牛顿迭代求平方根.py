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



# todo 二分方法


# 示例：求平方根
S = 3
result = sqrt_newton(S)
print(f"The square root of {S} is approximately {result}")
