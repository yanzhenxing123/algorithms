"""
@Author: yanzx
@Time: 2025/8/25 22:34 
@Description: 
"""
import numpy as np


def simple_mlp_demo():
    """超简单的 MLP 演示"""

    # 数据
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])  # XOR 问题

    # 参数 - 调整维度，不用转置
    W1 = np.random.randn(2, 3) * 0.1  # [2, 3] 而不是 [3, 2]
    b1 = np.zeros((1, 3))  # [1, 3] 而不是 [3, 1]
    W2 = np.random.randn(3, 1) * 0.1  # [3, 1] 而不是 [1, 3]
    b2 = np.zeros((1, 1))  # [1, 1]

    # 训练
    for epoch in range(1000):
        # 前向传播 - 直接矩阵乘法，不用转置
        Z1 = X @ W1 + b1  # [4, 2] @ [2, 3] + [1, 3] = [4, 3]
        A1 = 1 / (1 + np.exp(-Z1))  # [4, 3]
        Z2 = A1 @ W2 + b2  # [4, 3] @ [3, 1] + [1, 1] = [4, 1]
        A2 = 1 / (1 + np.exp(-Z2))  # [4, 1]

        # 反向传播
        dZ2 = A2 - y  # [4, 1] - [4, 1] = [4, 1]
        dW2 = A1.T @ dZ2  # [3, 4] @ [4, 1] = [3, 1]
        db2 = np.sum(dZ2, axis=0, keepdims=True)  # [1, 1]

        dZ1 = dZ2 @ W2.T * A1 * (1 - A1)  # [4, 1] @ [1, 3] * [4, 3] = [4, 3]
        dW1 = X.T @ dZ1  # [2, 4] @ [4, 3] = [2, 3]
        db1 = np.sum(dZ1, axis=0, keepdims=True)  # [1, 3]

        # 更新
        W2 -= 0.1 * dW2
        b2 -= 0.1 * db2
        W1 -= 0.1 * dW1
        b1 -= 0.1 * db1

        if epoch % 200 == 0:
            loss = np.mean((A2 - y) ** 2)
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

    # 测试
    Z1 = X @ W1 + b1
    A1 = 1 / (1 + np.exp(-Z1))
    Z2 = A1 @ W2 + b2
    A2 = 1 / (1 + np.exp(-Z2))

    print(f"\n预测结果:")
    for i in range(4):
        print(f"输入: {X[i]}, 真实: {y[i][0]:.2f}, 预测: {A2[i][0]:.2f}")


# 运行超简单演示
if __name__ == '__main__':
    simple_mlp_demo()
