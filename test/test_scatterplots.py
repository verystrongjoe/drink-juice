import pandas as pd
import matplotlib.pyplot as plt
import core.util.data as util
import numpy as np

def compute_daily_returns(df) :
    """
    Compute and return the daily return values
    :param df:
    :return:
    """
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) -1
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
    return daily_returns

def test_run() :

    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = util.get_data_with_mulitple_symbols(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)


    # Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    idx = np.isfinite(daily_returns['SPY']) & np.isfinite(daily_returns['SPY'])
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'][idx], daily_returns['XOM'][idx], 1)
    print('beta_XOM=', beta_XOM)
    print('alpha_XOM=', alpha_XOM)
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY'] + alpha_XOM, '-', color='r')
    plt.show()

    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    idx = np.isfinite(daily_returns['SPY']) & np.isfinite(daily_returns['GLD'])
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'][idx], daily_returns['GLD'][idx], 1)

    print('beta_XOM=', beta_XOM)
    print('alpha_XOM=', alpha_XOM)
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY'] + alpha_XOM, '-', color='r')

    plt.show()

    print(daily_returns.corr(method='pearson'))

if __name__ == '__main__' :
    test_run()