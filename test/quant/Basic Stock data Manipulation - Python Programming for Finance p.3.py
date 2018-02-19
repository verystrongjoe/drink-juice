import datetime as dt
from textwrap import indent

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

from matplotlib import style
import pandas as pd
import  pandas_datareader.data as web



style.use('ggplot')


# start = dt.datetime(2000,1,1)
# end = dt.datetime(2016,12,31)
# df = web.DataReader('TSLA', 'yahoo', start,end)
# df.to_csv('TSLA.csv')


df_from_csv = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)
# df_from_csv['100ma'] =  df_from_csv['Adj Close'].rolling(window=100, min_periods=0).mean()

df_ohlc =  df_from_csv['Adj Close'].resample('10D').ohlc()
df_volume = df_from_csv['Volume'].resample('10D').sum()

# print(df_ohlc.head())
# print(df_volume.head())

df_ohlc.reset_index(inplace=True)
df_ohlc_added = df_ohlc.assign(Date = lambda x : df_ohlc['Date'].map(lambda x: mdates.date2num(x)))
# df_ohlc['Date'].map(mdates.date2num) # it is not working
dh_ohlc = df_ohlc_added
print(df_ohlc_added.describe())


# print(df_from_csv.head(5))
# df_from_csv.dropna(inplace=True)


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()


# print(df_ohlc.values)
candlestick_ohlc(ax1, df_ohlc_added.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
plt.show()





# ax1.plot(df_from_csv.index, df_from_csv['Adj Close'])
# ax1.plot(df_from_csv.index, df_from_csv['100ma'])
# ax2.bar(df_from_csv.index, df_from_csv['Volume'])
#
# plt.show()


