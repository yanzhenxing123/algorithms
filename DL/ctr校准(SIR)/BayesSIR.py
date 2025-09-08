import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from beta import HyperParam
from utils import timer
import math
from typing import List, Dict
from metrics import cal_Cal_N, cal_GC_N
from SIR import SIR, get_data


class BayesSIR(SIR):
    def __init__(self, bin_size: int):
        super(BayesSIR, self).__init__(bin_size)

    def binning(self, data, K):
        """split data"""
        data_sorted = data.sort_values(by='pctr')
        df_li = np.array_split(data_sorted, K)
        BL = []
        for S in df_li:
            S_grouped = S.groupby("campaign_id")
            I = S_grouped['is_clicked'].count()
            C = S_grouped['is_clicked'].sum()
            hyper = HyperParam(1, 1)
            hyper.update_from_data_by_moment(I.values, C.values)

            pv = S['is_clicked'].count()
            clk = S['is_clicked'].sum()
            origin_ctr = clk / pv
            new_ctr = (clk + hyper.alpha) / (pv + hyper.alpha + hyper.beta)
            print(f"alpha: {hyper.alpha:.4f}, beta: {hyper.beta:.4f}, ctr:{origin_ctr:.4f}, new_ctr:{new_ctr:.4f}, pv: {pv}, click: {clk}")
            d = {
                "x_min": S['pctr'].min(),  # x_min,
                "x_max": S['pctr'].max(),  # x_max,
                # "y_mean": S['is_clicked'].mean(),  # y_mean,
                "y_mean": new_ctr,  # y_mean,
                "num": len(S)
            }
            BL.append(d)
        return BL


if __name__ == '__main__':

    df_train = get_data()
    pctr, is_clicked = df_train['pctr'].values, df_train['is_clicked'].values

    bin_size = len(df_train) // 100

    sir = BayesSIR(bin_size=bin_size)
    sir.fit(df_train)
    calibrated_probs = list(map(sir.predict, pctr))
    df_train['calibrated_probs'] = np.array(calibrated_probs)
    for N in range(2, 10):
        GC_N = cal_GC_N(df_train['campaign_id'].values, calibrated_probs, is_clicked, N)
        GC_N_without_cal = cal_GC_N(df_train['campaign_id'].values, df_train['pctr'].values, is_clicked, N)
        print(f'GC-{N} value: {GC_N:.4f}')
        print(f'GC_N_without_cal-{N} value: {GC_N_without_cal:.4f}')
        print("*" * 100)
