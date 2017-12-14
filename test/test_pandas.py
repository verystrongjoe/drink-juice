import pandas as pd
import matplotlib.pyplot as plt


def get_max_close(symbol):
    """
    Return the maximum closing value for stock indicated by symbol

    :param symbol:
    :return:
    """
    df = pd.read_csv("../data/raw/tkrcsv/history/{}.csv".format(symbol))
    return df['Close'].max()


def get_mean_volume(symbol):
    """
    Return mean volume for stock indicated by symbol

    :param symbol:
    :return:
    """
    df = pd.read_csv("../data/raw/tkrcsv/history/{}.csv".format(symbol))
    return df['Volume'].mean()

def test_run():
    df = pd.read_csv("../data/raw/tkrcsv/history/AAPL.csv")
    #print(df.head())
    #print(df.tail())
    #print(df[10:21])

def test_plot(symbol) :
    df = pd.read_csv("../data/raw/tkrcsv/history/{}.csv".format(symbol))
    #print(df['Adj Close'])
    df[['Close', 'Adj Close']].plot()
    plt.show()


def get_data_with_mulitple_symbols() :
    start_date = '2016-01-01'
    end_date = '2017-11-06'
    dates = pd.date_range(start_date, end_date)
    #print(dates)

    # Create an empty data frame
    df1 = pd.DataFrame(index=dates)

    # Read SPY data into temporary dataframe
    symbol = 'FB'
    dfFB = pd.read_csv("../data/raw/tkrcsv/history/{}.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'] )

    # Rename 'Adj Close' column to 'SPY' to prevent clash
    dfFB = dfFB.rename(columns={'Adj Close' : 'FB'})

    # print(dfFB.head())
    # df1 = df1.join(dfFB)
    df1 = df1.join(dfFB, how='inner')
    # print(df1)

    symbols =  ['AAPL', 'AMZN', 'MSFT']

    for symbol in symbols :
        df_temp = pd.read_csv("../data/raw/tkrcsv/history/{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df1 = df1.join(df_temp)

    #print(df1)

    return df1


def plot_data(df, title="Stock prices") :
    """
    Plot stock prices
    :param df:
    :return:
    """
    df.plot(title=title, fontsize=2)
    plt.show()

def normalize_data(df) :
    """
        Normalize stock price using the first row of the dataframe.
    :param df:
    :return:
    """
    return df /  df.ix[0,:]

if __name__ == "__main__" :
    #test_run()

    #pass
    #test_plot('AAPL')
    #for symbol in [ 'AAPL', 'AMZN'] :
    #    print( symbol, get_max_close(symbol))
    #    print( symbol, get_mean_volume(symbol))


    df = get_data_with_mulitple_symbols()
    #print(df.ix['2016-01-22':'2016-01-26']) # slice by row range(dates) using Dateframe.ix[] selector

    #print(df)

    #print('------------')

    #print(df['FB'])  # a single label selects a single column
    #print(df[['FB','AMZN']])
    #print(df.ix['2016-01-22':'2016-01-26', ['FB', 'AMZN']])
    # df.plot()
    # plt.show()

    print(df.head(3))
    print(df[1:].head(3))
    print(df[:-1].values)