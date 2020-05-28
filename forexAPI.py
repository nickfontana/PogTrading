import json
import requests
import oandapyV20
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.pricing as pricing
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

def get_account_summary():
    s = account.AccountSummary(accountID=ACCOUNT_ID)
    summary = api.request(s)
    return summary

