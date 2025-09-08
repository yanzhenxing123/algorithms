import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from utils import timer
import math
from typing import List, Dict
from metrics import cal_Cal_N, cal_GC_N


class SIR(object):
    def __init__(self, bin_size: int):
        self.bin_size = bin_size
        self.ML = []  # record function parameters

    def binning(self, data, K):
        """split data"""
        data_sorted = data.sort_values(by='pctr')
        df_li = np.array_split(data_sorted, K)
        BL = []
        for S in df_li:
            d = {
                "x_min": S['pctr'].min(),  # x_min,
                "x_max": S['pctr'].max(),  # x_max,
                "y_mean": S['is_clicked'].mean(),  # y_mean,
                "num": len(S)
            }
            BL.append(d)
        return BL

    def PAV_algo(self, BL: List[Dict]):
        """
        merge BL by y_mean
        :param BL:
        :return:
        """
        IBL = []
        for i in range(len(BL)):
            d = BL[i]
            li, ui, vi, ci = d['x_min'], d['x_max'], d['y_mean'], d['num']
            if not IBL:
                IBL.append(d)
                continue
            while IBL and vi <= IBL[-1]['y_mean']:  # y_mean_i < y_mean_i-1，merge
                d = IBL.pop()
                lt, ut, vt, ct = d['x_min'], d['x_max'], d['y_mean'], d['num']
                li = lt
                vi = (vi * ci + vt * ct) / (
                        ci + ct
                )  # vi = (y_mean_i * len(S_i) + y_mean_i+1 * len(S_i + 1)) / (len(S_i) + len(S_i+1))
                ci += ct
            IBL.append({
                "x_min": li,  # x_min,
                "x_max": ui,  # x_max,
                "y_mean": vi,  # y_mean,
                "num": ci
            })
        return IBL

    def interpolation(self, IBL: List[Dict]):
        """
        Calculate the slope and intercept of each piecewise function
        :param IBL:
        :return:
        """
        for i in range(len(IBL) - 1):
            d, d_next = IBL[i], IBL[i + 1]
            li, ui, vi, ci = d['x_min'], d['x_max'], d['y_mean'], d['num']
            li_next, ui_next, vi_next, ci_next = d_next['x_min'], d_next['x_max'], d_next['y_mean'], d_next['num']
            mi = (li + ui) / 2
            mi_next = (li_next + ui_next) / 2
            a = (vi_next - vi) / (mi_next - mi)
            b = vi - a * mi
            self.ML.append({
                "x_min": li,  # x_min,
                "x_max": ui,  # x_max,
                "a": a,
                "b": b
            })

    @timer
    def fit(self, data: pd.DataFrame):
        """
        Fit the model according to the given training data
        :param data:
        :return:
        """
        K = len(data) // self.bin_size
        BL = self.binning(data, K)
        IBL = self.PAV_algo(BL)
        print(len(IBL))
        self.interpolation(IBL)

    def predict(self, x):
        """
        Predict using the linear model
        :param x:
        :return:
        """
        if not self.ML:
            raise AssertionError("Please train first")
        for d_ in self.ML:
            li, ui, a, b = d_['x_min'], d_['x_max'], d_['a'], d_['b']
            if li <= x <= ui:
                return a * x + b
        # Handle edge cases where x is outside the range of the bins
        if x < self.ML[0]['x_min']:  # x < x_min
            return self.ML[0]['a'] * x + self.ML[0]['b']  # min f(x)
        if x > self.ML[-1]['x_max']:  # x > x_max
            return self.ML[-1]['a'] * x + self.ML[-1]['b']  # max f(x)
        return None


@timer
def get_data() -> pd.DataFrame:
    df = pd.read_csv("data/real_data_10000000.csv", sep="\t")
    df = df.dropna()

    df["campaign_id"] = df['app_id_core_model'].map(str) + "+" + df['unit_id'].map(str) + "+" + df[
        'big_template_id'].map(str)
    df = df.rename(columns={"p_ivr": "pctr", "cvr_label": "is_clicked"})
    df_train = df
    # df_train, df_test = train_test_split(df, test_size=0.02, random_state=100)
    grouped = df_train.groupby('campaign_id')['is_clicked'].sum()
    df_ins_gt10 = grouped[grouped > 10]
    df_train = df_train[df['campaign_id'].isin(df_ins_gt10.index.to_list())]
    return df_train


if __name__ == '__main__':
    # 示例数据
    # df = pd.read_csv(
    #     "data/ecpm_10000000.csv",
    # )

    df_train = get_data()
    pctr, is_clicked = df_train['pctr'].values, df_train['is_clicked'].values

    bin_size = len(df_train) // 100

    sir = SIR(bin_size=bin_size)
    sir.fit(df_train)
    calibrated_probs = list(map(sir.predict, pctr))
    df_train['calibrated_probs'] = np.array(calibrated_probs)

    # compute GC-N
    # N = len(T_train) // bin_size  # 设定分bin数
    for N in range(2, 10):
        GC_N = cal_GC_N(df_train['campaign_id'].values, calibrated_probs, is_clicked, N)
        GC_N_without_cal = cal_GC_N(df_train['campaign_id'].values, df_train['pctr'].values, is_clicked, N)
        print(f'GC-{N} value: {GC_N:.4f}')
        print(f'GC_N_without_cal-{N} value: {GC_N_without_cal:.4f}')
        print("*" * 100)
