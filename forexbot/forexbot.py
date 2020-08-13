import time
import schedule
from datetime import datetime
from threading import Timer, Event
from forexAPI import *


# nohup python3 -u forexBOT.py > output.log &


# EURUSD / USDJPY / GBPUSD / AUDUSD / USDCAD / EUR/JPY / NZD/USD
# market open from 4pm cst sunday to 3pm cst friday
# daily candles start at 9pm cst
# most trades take place between 7am and 11am cst
# test with trading 24 hours from 9:01 PM to 8:59 PM cst
# test with trading 4 hours starting at 7:01 AM to 10:59 AM cst



def bot():
    print("Starting...\n")
    n = 7
    runtime = 0
    if datetime.today().weekday() == 3:
        runtime = 21540
    averages = {
        'EUR_USD': ADR('eur', 'usd', n, 5),
        'USD_JPY': ADR('usd', 'jpy', n, 3),
        'GBP_USD': ADR('gbp', 'usd', n, 5),
        'AUD_USD': ADR('aud', 'usd', n, 5),
        'USD_CAD': ADR('usd', 'cad', n, 5),
        'EUR_JPY': ADR('eur', 'jpy', n, 3),
        'NZD_USD': ADR('nzd', 'usd', n, 5)
    }

    # For testing instance log; delete eventually
    print(datetime.now().strftime("%Y-%m-%d %H:%M"))
    for instrument in averages.keys():
        print(instrument, "OPEN:")
        precision = averages[instrument]['precision']
        print(round(averages[instrument]['todays_open'], precision),"\n")
    while True:
        if datetime.now().hour == 20:
            if datetime.now().minute == 59:
                print("End of day... restarting")
                print(datetime.now().strftime("%Y-%m-%d %H:%M"))
                return
        #if runtime >= 86340:
         #   print("End of day... restarting")
          #  return
        summary = GET_ACCOUNT_SUMMARY()['account']
        buying_power = float(summary['marginAvailable'])
        if buying_power <= 100:
            print("Buying power low... exiting")
            return
        for instrument in averages.keys():
            #print("Checking " + str(instrument + " ...\n"))
            precision = averages[instrument]['precision']
            todays_open = round(averages[instrument]['todays_open'], precision)
            currPrice = round(GET_CURRENT_PRICE(instrument), precision)
            sell_point = round(todays_open*(1+(0.5*averages[instrument]['avg_high'])), precision)
            buy_point = round(todays_open*(1-(0.5*averages[instrument]['avg_low'])), precision)
            stop_loss = round(todays_open*(1-(2*averages[instrument]['avg_low'])), precision)
            if currPrice <= buy_point:
                #if not CURRENTLY_OWNED(instrument):
                units = int((buying_power/4)/currPrice)
                if averages[instrument]['precision'] == 3:
                    units = units*100
                PLACE_LIMIT_ORDER(instrument, units, buy_point, sell_point, stop_loss)
                del averages[instrument]
                break
        time.sleep(5)
        #runtime += 5


schedule.every().sunday.at('21:01').do(bot)
schedule.every().monday.at('21:01').do(bot)
schedule.every().tuesday.at('21:01').do(bot)
schedule.every().wednesday.at('21:01').do(bot)
schedule.every().thursday.at('21:01').do(bot)


def test_():
    n = 0
    while True:
        print(n, 'BUYING')
        PLACE_LIMIT_ORDER('EUR_USD', 1, '1.2645', '1.2660')
        n += 1
        time.sleep(10)


def main():
    # unnecessary unless another thread is added
    #event = Event()
    #Timer(1, bot).start()
    #event.set()
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == '__main__':
    main()
