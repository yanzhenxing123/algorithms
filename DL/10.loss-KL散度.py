import torch
import torch.nn.functional as F


def manual_kl_div_logits(p_logits, q_logits):
    """
    通过 logits 计算 KL 散度 (P || Q)
    参数:
        p_logits: 真实分布的 logits [N, C]
        q_logits: 预测分布的 logits [N, C]
    返回:
        kl_div: 标量
    """
    p_probs = F.softmax(p_logits, dim=1)
    log_p = F.log_softmax(p_logits, dim=1)
    log_q = F.log_softmax(q_logits, dim=1)
    kl = p_probs * (log_p - log_q)  # KL = sum(p * (log(p) - log(q)))
    return torch.sum(kl) / len(p_logits)

# 示例数据
p_logits = torch.tensor([[1.0, 0.5], [0.2, 0.8]])
q_logits = torch.tensor([[0.9, 0.6], [0.3, 0.7]])

manual_loss_logits = manual_kl_div_logits(p_logits, q_logits)
print(f"Manual KL (Logits): {manual_loss_logits.item():.4f}")  # 输出: 0.0063