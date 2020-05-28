import time
#from contextlib import contextmanager
from api import *

# change to just use buy/sell limits

#@contextmanager
def marginBot(stock, margins):
    qty = 1
    buying, selling = True, True
    bought, sold = False, False
    boughtPrice, soldPrice = 0,0
    initPrice = get_current_stock_price(stock)
    while buying:
        print(str(time.asctime(time.localtime(time.time()))) + ': processing order')
        #start = time.time()
        currPrice = get_current_stock_price(stock)
        if initPrice*(1-margins) >= currPrice:
            make_order(stock, qty, "buy", "market", "day")
            buying = False
            bought = True
            boughtPrice = currPrice
        time.sleep(10)
    if bought == False:
        return "Failed to place buy order"
    initPrice = get_current_stock_price(stock)
    while selling:
        #start = time.time()
        currPrice = get_current_stock_price(stock)
        if currPrice >= initPrice*(1+margins):
            make_order(stock, qty, "sell", "market", "day")
            selling = False
            sold = True
            soldPrice = currPrice
        time.sleep(10)
    if sold == False:
        return "Failed to place sell order"
    return "Bought " + stock + "at " + str(boughtPrice) + "\n" + "Sold " + stock + "at " + str(soldPrice)
