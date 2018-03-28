## https://docs.gdax.com/?python#get-product-order-book

import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=3)


print('---------------------------')

print('level2 - top 50 bids and asks')


res = requests.get('https://api.gdax.com/products/BTC-USD/book', params={'level':2})

pp.pprint(json.loads(res.text))


# print('---------------------------')
# print('Full order book(non aggregated')
#
# res = requests.get('https://api.gdax.com/products/BTC-USD/book', params={'level':3})
#
# pp.pprint(json.loads(res.text))