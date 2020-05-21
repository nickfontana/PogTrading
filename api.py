import requests
import json
import alpaca_trade_api as tradeapi
#from googlefinance import getQuotes
from accountConfig import KEY, SECRET_KEY, ENDPOINT

ACCOUNT_URL = "{}/v2/account".format(ENDPOINT)
ORDERS_URL = "{}/v2/orders".format(ENDPOINT)
POSITIONS_URL = "{}/v2/positions".format(ENDPOINT)
ASSETS_URL = "{}/v2/assets".format(ENDPOINT)
CLOCK_URL = "{}/v2/clock".format(ENDPOINT)
PORTFOLIO_HISTORY_URL = "{}/v2/account/portfolio/history".format(ENDPOINT)
HEADERS = {'APCA-API-KEY-ID': KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
BARS_ENDPOINT = "https://data.alpaca.markets/v1"
BARS_URL = "{}/bars/1Min".format(BARS_ENDPOINT)
api_BARS = tradeapi.REST(KEY, SECRET_KEY, BARS_ENDPOINT)
api = tradeapi.REST(KEY, SECRET_KEY, ENDPOINT)

def make_order(symbol, qty, side, type, time_in_force):
    vals = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force,
       # "limit_price": limit_price,
       # "stop_price": stop_price
    }

    req = requests.post(ORDERS_URL, json=vals, headers=HEADERS)
    return json.loads(req.content)
    
def get_positions():
    req = requests.get(POSITIONS_URL, headers=HEADERS)
    return json.loads(req.content)

def get_order_history():
    req = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(req.content)

def get_current_stock_price(symbol):
    #vals = {
     #   "symbols": symbol,
      #  "limit": 1,
    #}

    #req = requests.get(BARS_URL, json=vals, headers=HEADERS)
    #data = json.loads(req.content)
    #return data
    data = api.get_barset(symbol, '1Min', limit=1)[symbol]
    return data[0].c

#def get_avg_daily_fluctuation():




#make_order("TSLA", 1, "buy", "market", "day")
