#!/usr/bin/python3
from colored import fg, attr
from datetime import date
from dateutil.relativedelta import relativedelta
from yahoo_fin import stock_info as si

round_number = 2

def Run(ticker1, ticker2, ticker3, ticker4, ticker5):
    print_ticker_info(ticker1)
    print_ticker_info(ticker2)
    print_ticker_info(ticker3)
    print_ticker_info(ticker4)
    print_ticker_info(ticker5)

def print_ticker_info(ticker):
    if ticker is not None:
        ticker_price = si.get_live_price(ticker)
        output = ticker.split('.', 1)[0] + ': ' + str(round(ticker_price, round_number))
        print(f"{fg(3)}{output}{get_dividends(ticker)}{attr(0)}")
        print_change(ticker, ticker_price)

def get_dividends(ticker):
    try:
        today = date.today()
        last_year = today + relativedelta(years=-1)
        dividends = si.get_dividends(ticker, start_date = last_year, end_date = today, index_as_date = True)
        return " - Dividends (12 months): {}".format(round(dividends['dividend'].sum(), round_number))
    except Exception:
        return ""

def print_change(ticker, ticker_price):
    previous_close = si.get_quote_table(ticker, dict_result = True).get('Previous Close')
    change = ticker_price - previous_close
    change_percentage = "{}%".format(round(100 - (previous_close*100/ticker_price), round_number))
    if(change > 0):
        print(f"  => Change: {fg(2)}{round(change, round_number)} ({change_percentage}){attr(0)}")
    else:
        print(f"  => Change: {fg(1)}{round(change, round_number)} ({change_percentage}){attr(0)}")