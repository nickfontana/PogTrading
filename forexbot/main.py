import time
import schedule

def run_all():
	bot1()
	bot2()
	bot3()

schedule.every().sunday.at('21:01').do(run_all)
schedule.every().monday.at('21:01').do(run_all)
schedule.every().tuesday.at('21:01').do(run_all)
schedule.every().wednesday.at('21:01').do(run_all)
schedule.every().thursday.at('21:01').do(run_all)

def main():
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == '__main__':
    main()