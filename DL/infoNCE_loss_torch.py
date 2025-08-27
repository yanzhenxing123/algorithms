import torch
import torch.nn.functional as F


def info_nce_loss(features, temperature=0.07):
    """
    简洁的InfoNCE loss实现，适合面试
    
    Args:
        features: 特征向量 [2N, D] - 每两个样本是一对正样本
        temperature: 温度参数，控制softmax的平滑程度
    
    Returns:
        loss值
    """
    # 1. 特征归一化
    features = F.normalize(features, dim=1)
    
    # 2. 计算相似度矩阵
    sim_matrix = torch.matmul(features, features.T) / temperature
    
    # 3. 创建正样本对的mask
    batch_size = features.shape[0]
    pos_mask = torch.zeros_like(sim_matrix, dtype=torch.bool)
    for i in range(0, batch_size, 2):
        pos_mask[i, i+1] = True
        pos_mask[i+1, i] = True
    
    # 4. 对每个样本，计算损失
    loss = 0
    for i in range(batch_size):
        # 获取当前样本与所有样本的相似度
        sim_i = sim_matrix[i]
        
        # 正样本相似度（当前样本的正样本对）
        if i % 2 == 0:
            pos_sim = sim_i[i+1]  # 与配对样本的相似度
        else:
            pos_sim = sim_i[i-1]  # 与配对样本的相似度
        
        # 负样本相似度（排除自己和正样本对）
        neg_sim = []
        for j in range(batch_size):
            if j != i and not pos_mask[i, j]:
                neg_sim.append(sim_i[j])
        
        if neg_sim:
            neg_sim = torch.stack(neg_sim)
            
            # 构建logits: [正样本相似度, 负样本相似度...]
            logits = torch.cat([pos_sim.unsqueeze(0), neg_sim])
            
            # 标签是0，因为正样本在第一个位置
            labels = torch.zeros(1, dtype=torch.long, device=features.device)
            
            # 计算交叉熵损失
            loss += F.cross_entropy(logits.unsqueeze(0), labels)
    
    return loss / batch_size


# 更简洁的版本（推荐面试用）
def info_nce_loss_simple(features, temperature=0.07):
    """
    最简洁的InfoNCE loss实现
    """
    # 归一化
    features = F.normalize(features, dim=1)
    
    # 计算相似度
    sim = torch.matmul(features, features.T) / temperature
    
    # 正样本对：相邻两个样本
    pos_sim = torch.diag(sim, 1)[::2]  # 取上对角线的值
    
    # 负样本：除了正样本对之外的所有相似度
    mask = torch.eye(features.shape[0], dtype=torch.bool)
    for i in range(0, features.shape[0], 2):
        mask[i, i+1] = True
        mask[i+1, i] = True
    
    neg_sim = sim[~mask].view(features.shape[0], -1)
    
    # 构建logits: [正样本, 负样本...]
    logits = torch.cat([pos_sim.unsqueeze(1), neg_sim], dim=1)
    
    # 标签都是0（正样本在第一个位置）
    labels = torch.zeros(features.shape[0], dtype=torch.long, device=features.device)
    
    return F.cross_entropy(logits, labels)


# 测试代码
if __name__ == "__main__":
    # 创建测试数据
    batch_size = 6  # 3对正样本
    feature_dim = 64
    
    features = torch.randn(batch_size, feature_dim)
    
    # 测试两个版本
    loss1 = info_nce_loss(features)
    loss2 = info_nce_loss_simple(features)
    
    print(f"InfoNCE Loss (详细版): {loss1.item():.4f}")
    print(f"InfoNCE Loss (简洁版): {loss2.item():.4f}")
    
    # 验证梯度
    features.requires_grad_(True)
    loss = info_nce_loss_simple(features)
    loss.backward()
    print(f"梯度范数: {features.grad.norm().item():.4f}")

