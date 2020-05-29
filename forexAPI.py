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
    }
    req = instruments.InstrumentsCandles(instrument=instrumentName, params=params)
    data = api.request(req)
    candles = data['candles']
    percent_change = 0
    for candle in candles:
        high = float(candle['mid']['h'])
        low = float(candle['mid']['l'])
        open = float(candle['mid']['o'])
        percent_change += (high-low)/open

    avg_daily_range = percent_change/time_period
    return avg_daily_range*100
    # get candlesticks
    # calc daily ranges
    # calc avg daily range


def get_account_summary():
    s = account.AccountSummary(accountID=ACCOUNT_ID)
    summary = api.request(s)
    return summary


print(ADR('eur', 'usd', 14))