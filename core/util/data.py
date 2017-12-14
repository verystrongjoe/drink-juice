import pandas as pd
import matplotlib.pyplot as plt

def get_data_with_mulitple_symbols(symbols, dates) :
    # Create an empty data frame
    df1 = pd.DataFrame(index=dates)

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