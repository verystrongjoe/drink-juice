import gdax
import pprint

pp = pprint.PrettyPrinter(indent=4)
public_client = gdax.PublicClient()


# GDAX에서 거래되는 코인들에 대한 정보
pp.pprint(len(public_client.get_products()))
pp.pprint(public_client.get_products())

# 호가데이터 가져오는 부분
pp.pprint(public_client.get_product_order_book('BTC-USD', level=3))

# 티커정보 조회
pp.pprint(public_client.get_product_ticker(product_id='ETH-USD'))


# pp.pprint(print(public_client.get_product_historic_rates('ETH-USD')))
# To include other parameters, see function docstring:
# public_client.get_product_historic_rates('ETH-USD', granularity=3000)



# 24시간 통계 데이터
pp.pprint(public_client.get_product_24hr_stats('ETH-USD'))


# 시간
pp.pprint(public_client.get_time())

# 환율
pp.pprint(public_client.get_currencies())
