## https://docs.gdax.com/?python#get-trades
import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=3)

print('---------------------------')

print('trade inforamtion')

res = requests.get('https://api.gdax.com/products/BTC-USD/trades')

pp.pprint(json.loads(res.text))