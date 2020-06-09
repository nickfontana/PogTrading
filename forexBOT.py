import time
from threading import Timer, Event
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
        buying_power = float(summary['marginAvailable'])
        if buying_power <= 100:
            return
        for instrument in averages.keys():
            print("Checking " + str(instrument + " ...\n"))
            currPrice = round(GET_CURRENT_PRICE(instrument), 5)
            todays_open = round(averages[instrument]['recent_open'], 5)
            sell_point = round(todays_open*(1+averages[instrument]['avg_high']), 3)
            buy_point = round(todays_open*(1-averages[instrument]['avg_low']), 3)
            print(todays_open)
            print(currPrice)
            if currPrice <= buy_point:
                if not CURRENTLY_OWNED(instrument):
                    units = int((buying_power/4)/currPrice)
                    # IMPORTANT: units set to 1 for testing
                    # TODO: change @param units=units
                    PLACE_LIMIT_ORDER(instrument, 1, buy_point, sell_point)
                    done = True
                    return
        # set to 5 second delay for testing
        # TODO: change to 5 minutes
        time.sleep(5)



        # check prices of all pairs that aren't already owned
        # if price <= open*(1-low) :
        #   units = 25% of buying power worth
        #   PLACE_LIMIT_ORDER(instrument, units, open*(1-low), open*(1+high))



def main():
    # unnecessary unless another thread is added.. keep for now
    event = Event()
    Timer(1, bot).start()
    event.set()

    
if __name__ == '__main__':
    main()
