import multiprocessing
from forexAPI import *


# thread 1:
# check buying power flag
# remove any current positions from dictionary of pairs
# periodically check current price and buy based on ADR
# on order enable current positions flag
# on order set sell limit


# EURUSD / USDJPY / GBPUSD / AUDUSD / USDCAD / EUR/JPY / NZD/USD


def bot():
    n = 14
    done = False
    averages = {
        'EUR_USD': ADR('eur', 'usd', n),
        'USD_JPY': ADR('usd', 'jpy', n),
        'GBP_USD': ADR('gbp', 'usd', n),
        'AUD_USD': ADR('aud', 'usd', n),
        'USD_CAD': ADR('usd', 'cad', n),
        'EUR_JPY': ADR('eur', 'jpy', n),
        'NZD_USD': ADR('nzd', 'usd', n)
    }

    while not done:
        summary = GET_ACCOUNT_SUMMARY()['account']
        if float(summary['marginAvailable']) <= 1:
            return
        for instrument in averages.keys():
            currPrice = GET_CURRENT_PRICE(instrument)
            if currPrice <= averages[instrument]['recent_open']*(1-averages[instrument]['avg_low']):
                if not CURRENTLY_OWNED():
                    #  TODO: PLACE ORDER
                    done = True



        # check prices of all pairs that aren't already owned
        # if price <= open*(1-low) :
        #   units = 25% of buying power worth
        #   PLACE_LIMIT_ORDER(instrument, units, open*(1-low), open*(1+high))

    #PLACE_LIMIT_ORDER('EUR_USD', 1, 1.0, 1.1)
    #print(averages['USD_JPY'])


def main():
    bot()
    #print(GET_CURRENT_PRICE('EUR_USD'))

if __name__ == '__main__':
    main()