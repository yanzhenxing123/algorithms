"""
@Author: yanzx
@Time: 2025/8/25 23:22 
@Description: 
"""

import numpy as np


class LogisticRegression:
    """简洁的逻辑回归实现"""

    def __init__(self, input_dim, lr=0.01, epochs=1000):
        self.w = np.random.randn(input_dim, 1) * 0.01  # 权重
        self.b = 0.0  # 偏置
        self.lr = lr
        self.epochs = epochs
        self.losss = []

    def sigmoid(self, z):
        """Sigmoid激活函数"""
        return 1 / (1 + np.exp(-z))

    def forward(self, X):
        """前向传播"""
        Z = X @ self.w + self.b
        return self.sigmoid(Z)

    def compute_loss(self, A, y):
        """计算交叉熵损失"""
        epsilon = 1e-15
        A = np.clip(A, epsilon, 1 - epsilon)
        return -np.mean(y * np.log(A) + (1 - y) * np.log(1 - A))

    def backward(self, X, A, y):
        """反向传播计算梯度"""
        batch_size = y.shape[0]
        dZ = A - y  # 损失对Z的梯度
        dw = X.T @ dZ / batch_size
        db = np.sum(dZ) / batch_size
        return dw, db

    def train(self, X, y):
        """训练模型"""
        if y.ndim == 1:
            y = y.reshape(-1, 1)

        print(f"开始训练，数据形状: X={X.shape}, y={y.shape}")

        for i in range(self.epochs):
            # 前向传播
            A = self.forward(X)

            # 计算损失
            loss = self.compute_loss(A, y)
            self.losss.append(loss)

            # 反向传播
            dw, db = self.backward(X, A, y)

            # 更新参数
            self.w -= self.lr * dw
            self.b -= self.lr * db

            if i % 100 == 0:
                accuracy = np.mean((A >= 0.5) == y)
                print(f"Epoch {i:4d}: Loss={loss:.6f}, Acc={accuracy:.4f}")

        print(f"训练完成！最终损失: {self.losss[-1]:.6f}")
        return self.losss

    def predict(self, X, threshold=0.5):
        """预测"""
        probabilities = self.forward(X)
        predictions = (probabilities >= threshold).astype(int)
        return predictions, probabilities

    def evaluate(self, X, y):
        """评估模型"""
        predictions, _ = self.predict(X)
        if y.ndim == 1:
            y = y.reshape(-1, 1)

        accuracy = np.mean(predictions == y)
        return accuracy


# 测试
def test_lr():
    """测试逻辑回归"""

    # 生成数据
    np.random.seed(42)
    n_samples = 1000

    # 类别0：中心(0,0)
    X0 = np.random.randn(n_samples // 2, 2)
    y0 = np.zeros((n_samples // 2, 1))

    # 类别1：中心(3,3)
    X1 = np.random.randn(n_samples // 2, 2) + 3
    y1 = np.ones((n_samples // 2, 1))

    # 合并数据
    X = np.vstack([X0, X1])
    y = np.vstack([y0, y1])

    # 分割数据
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # 训练模型
    model = LogisticRegression(input_dim=2, lr=0.1, epochs=500)
    losss = model.train(X_train, y_train)

    # 评估
    train_acc = model.evaluate(X_train, y_train)

if __name__ == '__main__':
    test_lr()