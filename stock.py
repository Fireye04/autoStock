import yfinance as yf


# stock.fast_info output
#
# lazy-loading dict with keys = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice',
# 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 'regularMarketPreviousClose', 'shares',
# 'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone', 'twoHundredDayAverage', 'yearChange', 'yearHigh',
# 'yearLow']

# stock.info output
#
# broken


def buy():
    stock = yf.Ticker("INTC")

    price = stock.fast_info["lastPrice"]
    print(price)

    return [["INTC", price]]


def sell():
    return "INTC"


buy()
