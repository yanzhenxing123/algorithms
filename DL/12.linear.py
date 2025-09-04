def z_score_normalize(data):
    """Z-score标准化 - 纯Python实现"""
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std = variance ** 0.5

    normalized = [(x - mean) / std for x in data]
    return normalized, mean, std


def linear_regression_normalized(pairs):
    """使用标准化数据的线性回归"""
    # 分离x和y
    x_data = [pair[0] for pair in pairs]
    y_data = [pair[1] for pair in pairs]

    # 标准化
    x_norm, x_mean, x_std = z_score_normalize(x_data)
    y_norm, y_mean, y_std = z_score_normalize(y_data)

    # 创建标准化后的数据对
    normalized_pairs = list(zip(x_norm, y_norm))

    # 在标准化数据上训练
    a_norm, b_norm = linear(normalized_pairs)

    # 将参数转换回原始尺度
    # 原始: y = a*x + b
    # 标准化: y_norm = a_norm*x_norm + b_norm
    # 其中: x_norm = (x - x_mean)/x_std, y_norm = (y - y_mean)/y_std
    # 代入得: (y - y_mean)/y_std = a_norm*(x - x_mean)/x_std + b_norm
    # 整理得: y = (a_norm*y_std/x_std)*x + (b_norm*y_std + y_mean - a_norm*y_std*x_mean/x_std)

    a_original = a_norm * y_std / x_std
    b_original = b_norm * y_std + y_mean - a_norm * y_std * x_mean / x_std

    return a_original, b_original, a_norm, b_norm


def linear(pairs):
    """你的原始线性回归实现"""
    a, b = 0.2, 0.1
    lr = 0.1  # 可以用较大的学习率，因为数据已标准化
    for epoch in range(10000):
        for x, y in pairs:
            y_pred = a * x + b
            d_y_pred = -(y - y_pred)
            da = x * d_y_pred
            db = 1 * d_y_pred
            a = a - lr * da
            b = b - lr * db
    return a, b


def get_data():
    """生成测试数据"""
    li = []
    for i in range(100, 1000):  # 按你的要求修改范围
        li.append((i, i * 2 + 1))
    return li


# 测试
pairs = get_data()
a_orig, b_orig, a_norm, b_norm = linear_regression_normalized(pairs)

print("标准化线性回归结果:")
print(f"原始尺度参数: a = {a_orig:.6f}, b = {b_orig:.6f}")
print(f"标准化尺度参数: a = {a_norm:.6f}, b = {b_norm:.6f}")
print(f"理论值: a = 2.000000, b = 1.000000")
print(f"误差: a误差 = {abs(2 - a_orig):.6f}, b误差 = {abs(1 - b_orig):.6f}")

# 验证结果
print("\n验证前5个数据点:")
for i, (x, y) in enumerate(pairs[:5]):
    y_pred = a_orig * x + b_orig
    print(f"x={x}, y={y}, y_pred={y_pred:.6f}, error={abs(y - y_pred):.6f}")

print("\n验证后5个数据点:")
for i, (x, y) in enumerate(pairs[-5:]):
    y_pred = a_orig * x + b_orig
    print(f"x={x}, y={y}, y_pred={y_pred:.6f}, error={abs(y - y_pred):.6f}")

# 对比：不使用标准化的结果
print("\n" + "=" * 60)
print("对比：不使用标准化的结果")
try:
    a_no_norm, b_no_norm = linear(pairs)
    print(f"无标准化结果: a = {a_no_norm}, b = {b_no_norm}")
except:
    print("无标准化结果: 数值不稳定，出现nan")

# 显示标准化前后的数据范围
print("\n" + "=" * 60)
print("数据标准化效果:")
x_data = [pair[0] for pair in pairs]
y_data = [pair[1] for pair in pairs]

print(f"原始x范围: {min(x_data)} ~ {max(x_data)}")
print(f"原始y范围: {min(y_data)} ~ {max(y_data)}")

x_norm, x_mean, x_std = z_score_normalize(x_data)
y_norm, y_mean, y_std = z_score_normalize(y_data)

print(f"标准化x范围: {min(x_norm):.3f} ~ {max(x_norm):.3f}")
print(f"标准化y范围: {min(y_norm):.3f} ~ {max(y_norm):.3f}")
print(
    f"标准化x均值: {sum(x_norm) / len(x_norm):.3f}, 标准差: {(sum((x - sum(x_norm) / len(x_norm)) ** 2 for x in x_norm) / len(x_norm)) ** 0.5:.3f}")
print(
    f"标准化y均值: {sum(y_norm) / len(y_norm):.3f}, 标准差: {(sum((y - sum(y_norm) / len(y_norm)) ** 2 for y in y_norm) / len(y_norm)) ** 0.5:.3f}")
