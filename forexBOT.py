import multiprocessing
from forexAPI import *


# thread 1:
# check buying power flag
# remove any current positions from dictionary of pairs
# periodically check current price and buy based on ADR
# on order enable current positions flag
# on order set sell limit


# EURUSD / USDJPY / GBPUSD / AUDUSD / USDCAD / EUR/JPY / NZD/USD


if __name__ == '__main__':
    n = 14
    averages = {
        'EUR_USD': ADR('eur', 'usd', n),
        'USD_JPY': ADR('usd', 'jpy', n),
        'GBP_USB': ADR('gbp', 'usd', n),
        'AUD_USD': ADR('aud', 'usd', n),
        'USD_CAD': ADR('usd', 'cad', n),
        'EUR_JPY': ADR('eur', 'jpy', n),
        'NZD_USD': ADR('nzd', 'usd', n)
    }
    PLACE_LIMIT_ORDER('EUR_USD', 1, 1.0, 1.1)
    #print(averages['EUR_USD'])