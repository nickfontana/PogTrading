import json
import requests
from datetime import datetime, timedelta
import oandapyV20
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as account

TOKEN = "b7763654ef81a5fa90c7f1aae2bfcb12-10f24e383660aab1f10696258a9e3d1f"
ACCOUNT_ID = "101-001-15011208-001"

HEADERS = {
    'Authorization' : 'Bearer ' + TOKEN,
}

ENDPOINT = "https://api-fxtrade.oanda.com"
PRICES_URL = ""
ACCOUNT_URL = ENDPOINT + "/v3/accounts/" + ACCOUNT_ID + "/summary"
ORDERS_URL = ENDPOINT + "/v3/accounts/" + ACCOUNT_ID + "/orders"

api = oandapyV20.API(access_token=TOKEN)

# calculates average daily range
# @param time_period: range of time in days
def ADR(base, quote, time_period):
    base = base.upper()
    quote = quote.upper()
    instrumentName = base + "_" + quote
    end = datetime.now()
    start = str((end - timedelta(days=time_period))).replace(" ", "T") + "Z"
    end = str(end).replace(" ", "T") + "Z"
    params = {
        "granularity": "D",
        "from": start,
        "to": end,
        "price": 'M'
    }
    req = instruments.InstrumentsCandles(instrument=instrumentName, params=params)
    data = api.request(req)
    candles = data['candles']
    total_change, high_change, low_change = 0, 0, 0
    today = candles[len(candles)-1]
    todays_open = today['mid']['o']
    for candle in candles:
        high = float(candle['mid']['h'])
        low = float(candle['mid']['l'])
        open = float(candle['mid']['o'])
        total_change += (high-low)/open
        high_change += (high-open)/open
        low_change += (open-low)/open

    avg_daily_range = total_change/time_period
    avg_high_range = high_change/time_period
    avg_low_range = low_change/time_period
    avgs = {
        'avg_daily_range': avg_daily_range*100,
        'avg_high': avg_high_range*100,
        'avg_low': avg_low_range*100,
        'recent_open': todays_open
    }
    return avgs
    # get candlesticks
    # calc daily ranges
    # calc avg daily range


def GET_ACCOUNT_SUMMARY():
    s = account.AccountSummary(accountID=ACCOUNT_ID)
    summary = api.request(s)
    return summary


# places a market buy order for @units units of @instrument at price @buy
# places a stop loss at price @sell
def PLACE_LIMIT_ORDER(instrument, units, buy, sell):
    params = {
        "order": {
            "type": 'LIMIT',
            "instrument": instrument,
            "units": units,
            "price": buy,
            "stopLossOnFill": {
                "timeInForce": 'GTC',
                "price": sell
            },
            "timeInForce": 'GTC',
            "positionFill": 'DEFAULT',
            "triggerCondition": 'DEFAULT'
        }
     }
    req = orders.OrderCreate(accountID=ACCOUNT_ID, data=params)
    api.request(req)



#print(ADR('eur', 'usd', 14))