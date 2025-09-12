"""
@Time: 2024/8/3 17:26
@Author: yanzx
@Desc:

GAUC = Σ (权重_i * AUC_i) / Σ (权重_i)

"""

import numpy as np
import torch
from collections import defaultdict


def get_roc_auc1(y_true, y_score):
    """
    O(m*n)
    :param y_true:
    :param y_score:
    :return:
    """
    gt_pred = list(zip(y_true, y_score))
    probs = []
    pos_samples = [x for x in gt_pred if x[0] == 1]
    neg_samples = [x for x in gt_pred if x[0] == 0]

    # 计算正样本大于负样本的概率
    for pos in pos_samples:  # 正样本和负样的组合
        for neg in neg_samples:
            if pos[1] > neg[1]:
                probs.append(1)
            elif pos[1] == neg[1]:
                probs.append(0.5)
            else:
                probs.append(0)

    return np.mean(probs)


def get_roc_auc2(y_true, y_score):
    """
    用公式计算
    :param y_true:
    :param y_score:
    :return:
    """
    y_true_score_tuple = list(zip(y_true, y_score))
    # 按照分排序
    y_true_score_tuple_sorted = sorted(y_true_score_tuple, key=lambda x: x[-1])
    ranks = list(enumerate(y_true_score_tuple_sorted, start=1))

    # 挑选出正样本的rank
    pos_ranks = [x[0] for x in ranks if x[1][0] == 1]
    M = sum(y_true)  # 正样本的数量
    N = len(y_true) - M  # 负样本的数量

    if M == 0 or N == 0:
        return 0.5  # 无法计算AUC时返回0.5

    auc = (sum(pos_ranks) - M * (M + 1) / 2) / (M * N)
    return auc


def calculate_gauc(y_true, y_score, group_ids, weight_type='impression', auc_method=get_roc_auc2):
    """
    计算GAUC (Group-wise AUC)

    Args:
        y_true: 真实标签列表 (0或1)
        y_score: 模型预测得分/概率列表
        group_ids: 分组ID列表 (如用户ID)
        weight_type: 权重类型 - 'impression'(曝光次数) 或 'click'(点击次数)
        auc_method: AUC计算方法，默认为get_roc_auc2

    Returns:
        float: GAUC值
        dict: 各组的详细AUC信息
    """
    # 按group_id组织数据
    groups = defaultdict(lambda: {'y_true': [], 'y_score': []})

    for i in range(len(y_true)):
        group_id = group_ids[i]
        groups[group_id]['y_true'].append(y_true[i])
        groups[group_id]['y_score'].append(y_score[i])

    total_auc = 0.0
    total_weight = 0.0
    group_results = {}

    # 逐组计算AUC
    for group_id, data in groups.items():
        group_y_true = data['y_true']
        group_y_score = data['y_score']

        # 计算权重
        if weight_type == 'impression':
            weight = len(group_y_true)  # 曝光次数作为权重
        elif weight_type == 'click':
            weight = sum(group_y_true)  # 点击次数作为权重
        else:
            raise ValueError("weight_type must be 'impression' or 'click'")

        # 检查是否有正负样本
        has_positive = any(label == 1 for label in group_y_true)
        has_negative = any(label == 0 for label in group_y_true)

        # 只有当该组有正负样本时才能计算AUC
        if has_positive and has_negative and weight > 0:
            try:
                auc = auc_method(group_y_true, group_y_score)
                total_auc += auc * weight
                total_weight += weight
                group_results[group_id] = {
                    'auc': auc,
                    'weight': weight,
                    'samples': len(group_y_true),
                    'clicks': sum(group_y_true)
                }
            except Exception as e:
                print(f"Warning: Could not calculate AUC for group {group_id}: {e}")
                continue

    if total_weight == 0:
        return 0.0, {}

    gauc = total_auc / total_weight
    return gauc, group_results


def print_gauc_summary(gauc, group_results):
    """打印GAUC结果摘要"""
    print(f"Overall GAUC: {gauc:.6f}")
    print(f"Number of valid groups: {len(group_results)}")

    if group_results:
        aucs = [info['auc'] for info in group_results.values()]
        weights = [info['weight'] for info in group_results.values()]

        min_auc = min(aucs)
        max_auc = max(aucs)
        avg_auc = sum(aucs) / len(aucs)

        # 计算加权平均AUC
        weighted_avg = sum(a * w for a, w in zip(aucs, weights)) / sum(weights)

        print(f"Min Group AUC: {min_auc:.6f}")
        print(f"Max Group AUC: {max_auc:.6f}")
        print(f"Average Group AUC: {avg_auc:.6f}")
        print(f"Weighted Average AUC: {weighted_avg:.6f}")


def generate_sample_data(n_samples=1000, n_users=3):
    """生成示例数据"""
    import random

    # 生成用户ID
    user_ids = [f"user{random.randint(1, n_users)}" for _ in range(n_samples)]

    # 生成标签和分数
    y_true = [random.randint(0, 1) for _ in range(n_samples)]
    y_score = [random.random() for _ in range(n_samples)]

    return y_true, y_score, user_ids


if __name__ == '__main__':
    # 测试AUC计算
    y_true = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    y_score = [0.1, 0.4, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 0.9, 0.9]

    print("AUC计算方法1:", get_roc_auc1(y_true, y_score))
    print("AUC计算方法2:", get_roc_auc2(y_true, y_score))
    print()

    # 测试GAUC计算
    print("GAUC测试:")
    y_true, y_score, user_ids = generate_sample_data(n_samples=100, n_users=5)

    # 计算GAUC - 按曝光次数加权
    gauc_impression, group_results = calculate_gauc(
        y_true, y_score, user_ids, weight_type='impression'
    )

    print_gauc_summary(gauc_impression, group_results)

    # 计算GAUC - 按点击次数加权
    gauc_click, _ = calculate_gauc(
        y_true, y_score, user_ids, weight_type='click'
    )
    print(f"\nGAUC (click-weighted): {gauc_click:.6f}")

    # 显示各组的详细结果
    print("\n各组详细结果:")
    for group_id, info in list(group_results.items())[:5]:  # 只显示前5组
        print(f"Group {group_id}: AUC={info['auc']:.6f}, "
              f"权重={info['weight']}, 样本数={info['samples']}, 点击={info['clicks']}")
