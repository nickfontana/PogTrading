import time
import schedule
from threading import Timer, Event
from forexAPI import *


# thread 1:
# check buying power flag
# remove any current positions from dictionary of pairs
# periodically check current price and buy based on ADR
# on order enable current positions flag
# on order set sell limit


# EURUSD / USDJPY / GBPUSD / AUDUSD / USDCAD / EUR/JPY / NZD/USD
# market open from 4pm cst sunday to 3pm cst friday
# daily candles start at 9pm cst
# most trades take place between 7am and 11am cst
# test with trading 24 hours from 9:01 PM to 8:59 PM cst
# test with trading 4 hours starting at 7:01 AM to 10:59 AM cst



def bot():
    n = 14
    done = False
    runtime = 0
    averages = {
        'EUR_USD': ADR('eur', 'usd', n, 5),
        'USD_JPY': ADR('usd', 'jpy', n, 3),
        'GBP_USD': ADR('gbp', 'usd', n, 5),
        'AUD_USD': ADR('aud', 'usd', n, 5),
        'USD_CAD': ADR('usd', 'cad', n, 5),
        'EUR_JPY': ADR('eur', 'jpy', n, 3),
        'NZD_USD': ADR('nzd', 'usd', n, 5)
    }
    while not done:
        if runtime >= 1435:
            return
        summary = GET_ACCOUNT_SUMMARY()['account']
        buying_power = float(summary['marginAvailable'])
        if buying_power <= 100:
            done = True
            return
        for instrument in averages.keys():
            #print("Checking " + str(instrument + " ...\n"))
            precision = averages[instrument]['precision']
            todays_open = round(averages[instrument]['todays_open'], precision)
            currPrice = round(GET_CURRENT_PRICE(instrument), precision)
            sell_point = round(todays_open*(1+averages[instrument]['avg_high']), precision)
            buy_point = round(todays_open*(1-averages[instrument]['avg_low']), precision)
            # print(todays_open)
            # print(currPrice)
            if currPrice <= buy_point:
                if not CURRENTLY_OWNED(instrument):
                    units = int((buying_power/4)/currPrice)
                    # units set to 1 for testing
                    PLACE_LIMIT_ORDER(instrument, units, buy_point, sell_point)
        time.sleep(5)
        runtime += 5


schedule.every().day.at('21:01').do(bot)


def main():
    # unnecessary unless another thread is added
    #event = Event()
    #Timer(1, bot).start()
    #event.set()
    while True:
        schedule.run_pending()
        time.sleep(5)


if __name__ == '__main__':
    main()
