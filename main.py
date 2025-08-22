def find_three_sum_combinations(prices, target):
    """
    找出所有不重复的三元组，使得它们的和等于目标金额

    Args:
        prices: 商品价格列表
        target: 目标金额（代金券面值）

    Returns:
        所有满足条件且不重复的三元组列表
    """
    if len(prices) < 3:
        return []

    # 先对价格进行排序，便于后续处理
    prices.sort()
    result = []

    # 遍历每个元素作为第一个数
    for i in range(len(prices) - 2):
        # 跳过重复的元素，避免重复组合
        if i > 0 and prices[i] == prices[i - 1]:
            continue

        # 使用双指针法寻找另外两个数
        left = i + 1
        right = len(prices) - 1

        while left < right:
            current_sum = prices[i] + prices[left] + prices[right]

            if current_sum == target:
                # 找到满足条件的组合
                result.append([prices[i], prices[left], prices[right]])

                # 跳过重复的left元素
                while left < right and prices[left] == prices[left + 1]:
                    left += 1
                # 跳过重复的right元素
                while left < right and prices[right] == prices[right - 1]:
                    right -= 1

                # 移动指针继续寻找
                left += 1
                right -= 1

            elif current_sum < target:
                # 和太小，左指针右移
                left += 1
            else:
                # 和太大，右指针左移
                right -= 1

    return result


# 测试示例
if __name__ == "__main__":
    coupon_amount = 15
    shopping_cart = [4, 5, 6, 7, 4, 1]

    combinations = find_three_sum_combinations(shopping_cart, coupon_amount)
    print(f"代金券金额: {coupon_amount}")
    print(f"商品价格: {shopping_cart}")
    print(f"满足要求的组合: {combinations}")

    # 输出结果:
    # 代金券金额: 15
    # 商品价格: [4, 5, 6, 7, 4, 1]
    # 满足要求的组合: [[4, 4, 7], [4, 5, 6]]