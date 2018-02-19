import data
import matplotlib.pyplot as plt
from zipline.api import order, symbol, record, order_target
from zipline.algorithm import TradingAlgorithm
from zipline_poloniex.utils import setup_logging
import logging

# 1일 = 86400 / 5분 = 300 / 15분 = 900
gs = data.DataReader(currencyPair='USDT_BTC',
                     excahge='Poloniex',
                     start='2017.01.10 00:00:00',
                     end='2018.01.12 00:00:00',
                     period=300).make()

print('[*] 데이터 기초 정보')
print(gs.info())

print('[*] 종가 데이터만 셋팅')
gsData = gs[['close']]
print(gsData.head())

print('[*] 종가 컬럼명 변경')
gsData.columns = ['BTC']
print(gsData.head())

print('[*] 인덱스 타임 세계표준시로 변경')
gsData = gsData.tz_localize("UTC")
print(gsData)

__author__ = "Florian Wilhelm"
__copyright__ = "Florian Wilhelm"
__license__ = "new-bsd"

# setup logging and all
setup_logging(logging.INFO)
_logger = logging.getLogger(__name__)
_logger.info("Dummy agent loaded")

def initialize(context):
    _logger.info("Initializing agent...")
    # There seems no "nice" way to set the emission rate to minute
    #context.sim_params._emission_rate = 'minute'
    context.i = 0
    context.sym = symbol('BTC')
    context.hold = False

def handle_data(context, data):
    _logger.debug("Handling data...")
    context.i += 1
    if context.i < 20:
        return
    order(symbol('BTC'), 1)


gsData.to_csv('data.csv', index=True)

print('[*] 백테스팅 시뮬레이션 실시')
algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data) # daily or minute / , data_frequency='minute'
result = algo.run(gsData)

print('[*] 백테스팅 시뮬레이션 결과')
print(result.head())

result['portfolio_value'].plot()
plt.show()