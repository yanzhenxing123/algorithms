"""
@Time: 2024/8/3 17:26
@Author: yanzx
@Desc: 
"""

import numpy as np
import torch


def get_roc_auc1(y_true, y_score):
    """
    O(m*n)
    :param y_true:
    :param y_score:
    :return:
    """
    

    gt_pred = list(zip(y_true, y_score))
    print(gt_pred)
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
    ranks = list(enumerate(sorted(zip(y_true, y_score), key=lambda x: x[-1]), start=1))

    y_true_score_tuple = list(zip(y_true, y_score))
    # 按照分排序
    y_true_score_tuple_sorted = sorted(y_true_score_tuple, key=lambda x: x[-1])
    ranks = list(enumerate(y_true_score_tuple_sorted, start=1))
    print(ranks)
    """
    ranks = [(1, (0, 0.1)),
             (2, (0, 0.4)),
             (3, (1, 0.6)),
             (4, (1, 0.6)),
             (5, (0, 0.7)),
             (6, (1, 0.7)),
             (7, (0, 0.8)),
             (8, (1, 0.8)),
             (9, (1, 0.9)),
             (10, (1, 0.9))]
    """
    # 挑选出正样本的rank
    pos_ranks = [x[0] for x in ranks if x[1][0] == 1]  # [3, 4, 6, 8, 9, 10]
    M = sum(y_true)  # 正样本rank的数量
    N = len(y_true) - M  # 负样本rank的数量
    auc = (sum(pos_ranks) - M * (M + 1) / 2) / (M * N)
    return auc


if __name__ == '__main__':
    y_true = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    y_score = [0.1, 0.4, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 0.9, 0.9]

    # print(get_roc_auc1(y_true, y_score))
    print(get_roc_auc2(y_true, y_score))
