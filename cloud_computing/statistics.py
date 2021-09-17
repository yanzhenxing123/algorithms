"""
@Author: yanzx
@Date: 2021-09-16 09:59:37
@Desc: 
"""

import pandas as pd
import numpy as np
import pandas_datareader
import itertools
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pylab import style
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm


style.use('ggplot')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
stockFile='./data_vegetable.csv'
data=pd.read_csv(stockFile,index_col=0,parse_dates=[0])
data.tail(10)
data=data[['price']].resample('W-MON').mean()
data=data.fillna(data.bfill())
data_train=data['2017':'2021']
data_train.plot(figsize=(15,8))
plt.legend(loc='upper left')
plt.title('vegetable price')
plt.xlabel('日期')
plt.ylabel('蔬菜价格')
sns.despine()
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
print('季节性 ARIMA 的参数选择:')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

warnings.filterwarnings("ignore")  # 忽视警告提示信息
for param in pdq:
    for param_seasonal in seasonal_pdq:
        mod = sm.tsa.statespace.SARIMAX(data_train,
                                    order=param,
                                    seasonal_order=param_seasonal,
                                    enforce_stationarity=False,
                                        enforce_invertibility=False)
        results = mod.fit()
        print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
model = sm.tsa.statespace.SARIMAX(data_train,
        order=(1, 0, 1),
        seasonal_order=(0, 1, 1, 12),
#         enforce_stationarity=False,
        enforce_invertibility=False)
results = model.fit()
print(results.summary())
results.plot_diagnostics(figsize=(15, 12))
plt.show()


pred=results.predict('2020','20210703',
                     dynamic=False,
                     typ='levels')
print(pred)
plt.figure(figsize=(15,4))
plt.xticks(rotation=45)
plt.plot(pred,label='Forecast')
plt.plot(data_train,label='True')
plt.xlabel('日期')
plt.ylabel('蔬菜价格')
plt.legend(loc='upper left')
plt.title('季节性 ARIMA--预测蔬菜价格随日期的变化关系')
plt.show()