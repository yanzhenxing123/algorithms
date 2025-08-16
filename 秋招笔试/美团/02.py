import numpy as np
import pandas as pd
import json
import sys


def gaussian_naive_bayes(train, test):
    # 转换为 numpy 数组
    train_data = np.array(train)
    test_data = np.array(test)

    # 分离特征和标签
    X_train = train_data[:, :-1]
    y_train = train_data[:, -1]

    # 获取类别
    classes = np.unique(y_train)
    n_classes = len(classes)
    n_features = X_train.shape[1]

    # 计算先验概率
    priors = np.zeros(n_classes)
    for i, c in enumerate(classes):
        priors[i] = np.sum(y_train == c) / len(y_train)

    # 计算每个类别的均值和方差
    means = np.zeros((n_classes, n_features))
    variances = np.zeros((n_classes, n_features))

    for i, c in enumerate(classes):
        X_c = X_train[y_train == c]
        means[i, :] = np.mean(X_c, axis=0)
        variances[i, :] = np.var(X_c, axis=0, ddof=0)

    # 处理方差为 0 的情况
    variances[variances == 0] = 1e-9

    # 预测
    predictions = []
    for x in test_data:
        log_probs = []
        for i, c in enumerate(classes):
            # 计算对数后验概率
            log_prior = np.log(priors[i])
            log_likelihood = -0.5 * np.sum(
                np.log(2 * np.pi * variances[i, :]) +
                ((x - means[i, :]) ** 2) / variances[i, :]
            )
            log_prob = log_prior + log_likelihood
            log_probs.append(log_prob)

        # 选择概率最大的类别
        pred = classes[np.argmax(log_probs)]
        predictions.append(int(pred))

    return predictions


if __name__ == "__main__":
    # 读取输入
    input_str = input()
    data = json.loads(input_str)

    train = data["train"]
    test = data["test"]

    # 预测
    predictions = gaussian_naive_bayes(train, test)

    # 输出结果
    print(json.dumps(predictions))