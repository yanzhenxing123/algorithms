"""
@Time: 2024/8/3 17:26
@Author: yanzx
@Desc: 
"""

import numpy as np


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
    for pos in pos_samples:
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
    ranks = enumerate(sorted(zip(y_true, y_score), key=lambda x: x[-1]), start=1)
    pos_ranks = [x[0] for x in ranks if x[1][0] == 1]
    M = sum(y_true)
    N = len(y_true) - M
    auc = (sum(pos_ranks) - M * (M + 1) / 2) / (M * N)
    return auc


if __name__ == '__main__':
    y_true = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    y_score = [0.1, 0.4, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8, 0.9, 0.9]

    print(get_roc_auc1(y_true, y_score))
    print(get_roc_auc2(y_true, y_score))

