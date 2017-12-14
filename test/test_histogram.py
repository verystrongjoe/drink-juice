import  pandas as pd
import  matplotlib.pyplot as plt


def get_data_with_mulitple_symbols(symbols, dates) :
    df1 = pd.DataFrame(index=dates)
    for symbol in symbols :
        df_temp = pd.read_csv("../data/raw/tkrcsv/history/{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df1 = df1.join(df_temp)
    return df1

def plot_data(df, title="Stock prices") :
    df.plot(title=title, fontsize=2)
    plt.show()


def test_run() :
    symbols = ['FB']
    dates = pd.date_range('2010-01-01', '2016-12-31')
    df = get_data_with_mulitple_symbols(symbols, dates)
    df_daily_returns = compute_daily_return(df)
    # plot_data(df)
    # plot_data(df_daily_returns)
    df_daily_returns.hist(bins=50)

    # Get mean and standard deviation
    mean = df_daily_returns['FB'].mean()
    print("mean=", mean)

    std = df_daily_returns['FB'].std()
    print("std=", std)

    # Compute kurtosis
    print(df_daily_returns.kurtosis())

    plt.axvline(mean, color='w', linestyle= 'dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)

    plt.show()





def compute_daily_return(df : pd.DataFrame) :
    """

    :param df:
    :return:
    """
    daily_returns = df.copy()
    daily_returns[1: ] = ( df[1: ] / df[:-1].values) -1
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
    return daily_returns


if __name__ == "__main__" :
    print('histogram!!')
    test_run()

