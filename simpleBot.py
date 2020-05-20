import requests
import json
import alpaca_trade_api as tradeapi
from accountConfig import KEY, SECRET_KEY, ENDPOINT

ACCOUNT_URL = "{}/v2/account".format(ENDPOINT)
ORDERS_URL = "{}/v2/orders".format(ENDPOINT)
POSITIONS_URL = "{}/v2/positions".format(ENDPOINT)
ASSETS_URL = "{}/v2/assets".format(ENDPOINT)
CLOCK_URL = "{}/v2/clock".format(ENDPOINT)
PORTFOLIO_HISTORY_URL = "{}/v2/account/portfolio/history".format(ENDPOINT)
HEADERS = {'APCA-API-KEY-ID': KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
#r = requests.get(ACCOUNT_URL, headers=HEADERS)
#print(json.loads(r.content))

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

#make_order("TSLA", 1, "buy", "market", "day")
print(get_order_history())

print(get_positions())
