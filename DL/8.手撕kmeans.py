import torch
import matplotlib.pyplot as plt


def kmeans(X, K, n_iter=20):
    # X: [N, D]
    N, D = X.shape
    # 随机初始化中心
    indices = torch.randperm(N)[:K]
    centers = X[indices].clone()
    for _ in range(n_iter):
        # 计算距离 [N, K]
        dist = torch.cdist(X, centers)
        # 分配每个点到最近中心
        labels = dist.argmin(dim=1)
        # 更新中心
        for k in range(K):
            if (labels == k).sum() > 0:
                centers[k] = X[labels == k].mean(dim=0)
    return centers, labels


# 简单测试
def simple_test():
    """简单的测试用例"""

    print("=== 简单K-Means测试 ===")

    # 生成测试数据：3个明显的簇
    torch.manual_seed(42)
    cluster1 = torch.randn(50, 2) + torch.tensor([0, 0])  # 中心在(0,0)
    cluster2 = torch.randn(50, 2) + torch.tensor([5, 5])  # 中心在(5,5)
    cluster3 = torch.randn(50, 2) + torch.tensor([0, 5])  # 中心在(0,5)

    X = torch.cat([cluster1, cluster2, cluster3], dim=0)

    print(f"数据: {X.shape[0]} 个点, {X.shape[1]} 维")
    print(f"期望: 3 个簇")

    # 运行K-Means
    centers, labels = kmeans(X, K=3, n_iter=20)

    # 显示结果
    unique_labels, counts = torch.unique(labels, return_counts=True)
    print(f"结果: {len(unique_labels)} 个簇")
    print(f"各簇大小: {counts.tolist()}")

    # 简单可视化
    plt.figure(figsize=(8, 6))

    colors = ['red', 'blue', 'green']
    for i in range(3):
        cluster_points = X[labels == i]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1],
                    c=colors[i], alpha=0.6, label=f'簇 {i}')

    # 画聚类中心
    plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x',
                s=200, linewidths=3, label='聚类中心')

    plt.title('K-Means 聚类结果')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    return X, centers, labels


# 边界测试
def edge_test():
    """边界情况测试"""

    print("\n=== 边界情况测试 ===")

    # 测试1：簇数=1
    print("测试1: 簇数=1")
    X = torch.randn(100, 2)
    centers, labels = kmeans(X, K=1, n_iter=10)
    print(f"  成功: {len(centers)} 个簇")

    # 测试2：簇数=数据点数
    print("测试2: 簇数=数据点数")
    X = torch.randn(5, 2)
    centers, labels = kmeans(X, K=5, n_iter=10)
    print(f"  成功: {len(centers)} 个簇")

    # 测试3：单点数据
    print("测试3: 单点数据")
    X = torch.randn(1, 2)
    centers, labels = kmeans(X, K=1, n_iter=10)
    print(f"  成功: {len(centers)} 个簇")


# 运行测试
if __name__ == "__main__":
    # 基本测试
    X, centers, labels = simple_test()

    # 边界测试
    edge_test()

    print("\n测试完成！")