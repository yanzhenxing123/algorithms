import torch


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


def rq_kmeans(X, K=256, L=2, n_iter=20):
    # X: [N, D]
    N, D = X.shape
    codes = []
    codebooks = []
    residual = X.clone()
    for l in range(L):
        centers, labels = kmeans(residual, K, n_iter)  # 16个label

        codebooks.append(centers)
        codes.append(labels)
        # 计算残差
        residual = residual - centers[labels]  # torch.Size([1000, 32]) - torch.Size([1000, 32])
    # codes: [L][N], codebooks: [L][K, D]
    return codes, codebooks


def rq_decode(codes, codebooks):
    # codes: [L][N], codebooks: [L][K, D]
    L = len(codes)
    N = codes[0].shape[0]
    D = codebooks[0].shape[1]
    X_rec = torch.zeros((N, D), device=codebooks[0].device)
    for l in range(L):
        X_rec += codebooks[l][codes[l]]

    return X_rec


# 示例
if __name__ == "__main__":
    torch.manual_seed(0)
    X = torch.randn(1000, 32)  # 1000个32维向量
    codes, codebooks = rq_kmeans(X, K=16, L=3, n_iter=10)

    X_rec = rq_decode(codes, codebooks)
    print("重构误差:", ((X - X_rec) ** 2).mean().item())  # torch.Size([1000, 32])

    # print(codebooks)
