import numpy as np
import pandas as pd

from beta import HyperParam
from utils import timer
import math


@timer
def cal_GC_N(campaign_id, pctr, is_clicked, N):
    """
    GC-N
    :param campaign_id:
    :param pctr:
    :param is_clicked:
    :param N:
    :return:
    """
    data = pd.DataFrame({
        "campaign_id": campaign_id,
        'pctr': pctr,
        'is_clicked': is_clicked
    })
    cal_Ns_weighted = []
    count = len(data)

    for index, df in data.groupby("campaign_id"):
        pctr_i = df['pctr'].values
        is_clicked_i = df['is_clicked'].values
        cal_N = cal_Cal_N(pctr_i, is_clicked_i, N)
        if math.isnan(cal_N):
            count -= len(df)
            continue
        cal_Ns_weighted.append(cal_N * len(df))
    GC_N = np.sum(cal_Ns_weighted) / count
    return GC_N


def cal_Cal_N(pctr, is_clicked, N, hyper=None):
    """
    Cal-N
    :param pctr:
    :param is_clicked:
    :param N:
    :return:
    """
    data = pd.DataFrame({
        'pctr': pctr,
        'is_clicked': is_clicked
    })
    data = data.sort_values(by='pctr')
    bins = np.array_split(data, N)

    errors = []
    for bin_data in bins:
        calibrated_ctr = bin_data['pctr'].mean()
        actual_ctr = bin_data['is_clicked'].mean()
        if not actual_ctr:
            continue
        pcoc = calibrated_ctr / actual_ctr
        if pcoc >= 1:
            error = pcoc - 1
        else:
            error = (1 / pcoc) - 1
        errors.append(error)
    rmse = np.sqrt(np.mean(np.array(errors) ** 2))
    return rmse
