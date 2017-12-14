import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_data_with_mulitple_symbols(symbols, dates) :
    # start_date = '2016-01-01'
    # end_date = '2017-11-06'
    # dates = pd.date_range(start_date, end_date)
    #print(dates)

    # Create an empty data frame
    df1 = pd.DataFrame(index=dates)

    #symbols =  ['AAPL', 'AMZN', 'MSFT']

    for symbol in symbols :
        df_temp = pd.read_csv("../data/raw/tkrcsv/history/{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df1 = df1.join(df_temp)

    return df1

def plot_data(df, title="Stock prices") :
    """
    Plot stock prices
    :param df:
    :return:
    """
    df.plot(title=title, fontsize=2)
    plt.show()

if __name__ == '__main__' :

    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['AAPL', 'AMZN', 'FB', 'BAC']
    df = get_data_with_mulitple_symbols(symbols, dates)
    plot_data(df)

    print(df.mean())