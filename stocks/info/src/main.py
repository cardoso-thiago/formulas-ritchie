#!/usr/bin/python3
import os

from formula import formula

ticker1 = os.environ.get("TICKER1")
ticker2 = os.environ.get("TICKER2")
ticker3 = os.environ.get("TICKER3")
ticker4 = os.environ.get("TICKER4")
ticker5 = os.environ.get("TICKER5")
formula.Run(ticker1, ticker2, ticker3, ticker4, ticker5)
