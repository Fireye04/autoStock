import math
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import yfinance as yf
from user import User
from web import getStockPrice


# stock.fast_info output
#
# lazy-loading dict with keys = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice',
# 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 'regularMarketPreviousClose', 'shares',
# 'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone', 'twoHundredDayAverage', 'yearChange', 'yearHigh',
# 'yearLow']

# stock.info output
#
# broken

def usdToShares(browser, ticker, usd, email, password):
    stockPrice = float(getStockPrice(browser, ticker, email, password))

    shares = math.ceil(usd / stockPrice)

    return shares


# TODO: buy by %
def buyStock(browser, ticker: str, numberOfShares: int, stockPrice, user, email, password):
    # stockPrice = round(yf.Ticker(ticker).fast_info["lastPrice"], 2)

    cost = stockPrice * numberOfShares

    reduct = 0
    if cost > user.buyingPower:

        while cost > user.buyingPower:
            cost -= stockPrice
            reduct += 1

        print(f"Provided shares cannot be purchased with current funds, reduced number of shares by "
              f"{reduct} or ${reduct * stockPrice} and continuing with purchase")

    # actual = getStockPrice(browser, ticker, email, password)
    #
    # print(f"yf = {stockPrice}, mw = {actual}")


def sellStock(self):
    pass


def main():
    browser = webdriver.Firefox()

    with open("Kai.p", "rb") as data:
        userr = pickle.load(data)

    with open("info.p", "rb") as data:
        info = pickle.load(data)

    userEmail = info[0]
    userPassword = info[1]

    ticker = "INTC"

    stockPrice = getStockPrice(browser, ticker, userEmail, userPassword)

    buyStock(browser, ticker, 99, userr, stockPrice, userEmail, userPassword)


if __name__ == "__main__":
    main()
