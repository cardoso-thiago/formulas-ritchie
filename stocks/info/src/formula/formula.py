#!/usr/bin/python3
from colored import fg, attr
from datetime import date
from dateutil.relativedelta import relativedelta
from yahoo_fin import stock_info as si

round_number = 2

def Run(ticker1, ticker2, ticker3, ticker4, ticker5):
    validate_ticker(ticker1)
    validate_ticker(ticker2)
    validate_ticker(ticker3)
    validate_ticker(ticker4)
    validate_ticker(ticker5)

def validate_ticker(ticker):
    if ticker is not None:
        print_ticker_info(ticker)

def print_ticker_info(ticker):
    dict_quote = si.get_quote_table(ticker, dict_result = True)
    current_price = dict_quote.get('Quote Price')
    previous_close = dict_quote.get('Previous Close')
    change = current_price - previous_close
    
    change_percentage = "{}%".format(round(100 - (previous_close*100/current_price), round_number))
    change_e = round(change, round_number)
    current_price_e = ticker.split('.', 1)[0] + ': ' + str(round(current_price, round_number))
    dividends = get_dividends(ticker)
    change_color = 3
    change_signal = ""

    if(change > 0):
        change_color = 2
        change_signal = "+"
    else:
        change_color = 1

    print(f"{fg(3)}{current_price_e} {fg(change_color)}{change_signal}{change_e}({change_percentage}){fg(3)}{dividends}{attr(0)}")

def get_dividends(ticker):
    try:
        today = date.today()
        last_year = today + relativedelta(years=-1)
        dividends = si.get_dividends(ticker, start_date = last_year, end_date = today, index_as_date = True)
        return " => Dividends (12 months): {}".format(round(dividends['dividend'].sum(), round_number))
    except Exception:
        return ""