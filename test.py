from forexAPI import *

def test():
    n=7
    averages = {
        'EUR_USD': ADR('eur', 'usd', n, 5),
        'USD_JPY': ADR('usd', 'jpy', n, 3),
        'GBP_USD': ADR('gbp', 'usd', n, 5),
        'AUD_USD': ADR('aud', 'usd', n, 5),
        'USD_CAD': ADR('usd', 'cad', n, 5),
        'EUR_JPY': ADR('eur', 'jpy', n, 3),
        'NZD_USD': ADR('nzd', 'usd', n, 5)
    }
    x = 3
    while x>0:
        for instrument in averages.keys():
            print(instrument, averages[instrument])
            del averages[instrument]
            break

        #del averages['USD_CAD']
        print("removed---------------------")
    
        for instrument in averages.keys():
            print(instrument, averages[instrument])

        x-=1

def main():
    test()

if __name__ == '__main__':
    main()
