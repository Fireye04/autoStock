import pickle
import yfinance as yf

class User:
    def __init__(self, userName: str, currentFunds: int, currentStockList: [[str, int], ...]):
        self.name = userName

        self.funds = currentFunds

        # paired list [stock: str, money in stock: int]
        self.stocks = currentStockList

        # just the strs
        self.plainStocks = []

        self.plainList()

        # calculates funds in stock
        self.fundsInStock = 0

        self.iterateFunds()

    def buyStock(self, ticker: str, numberOfShares: int):
        stok = yf.Ticker(ticker).fast_info["lastPrice"]


    def sellStock(self):
        pass

    def setFunds(self, amount: int, increment: bool):
        if increment:
            self.funds += amount
        else:
            self.funds = amount

    def setStocks(self, newStocks: [[str, int], ...]):
        self.stocks = newStocks

    def appendStocks(self, newStock: [str, int]):
        self.stocks.append(newStock)

    def removeStocks(self, remStock: str):
        for stock in self.stocks:
            if stock[0] == remStock:
                self.stocks.remove(stock)

    def plainList(self):
        self.plainStocks = []

        for i in range(len(self.stocks)):
            self.plainStocks.append(self.stocks[i][0])

    def iterateFunds(self):
        self.fundsInStock = 0

        # iterates over stockList and adds all stock values
        for i in range(len(self.stocks)):
            self.fundsInStock += self.stocks[i][1]

    def __str__(self):
        return f"{self.name}'s Stock Profile- \n~~~\nNet Worth- ${self.funds + self.fundsInStock} \n" \
               f"Funds- ${self.funds} \nMoney In Stocks- ${self.fundsInStock} \nStocks- {self.plainStocks} \n" \
               f"Paired Stocks- {self.stocks}"

# uncomment this to change the acting user
#
# user = User("Name", 100_000, [[]])
# with open(user.name + ".p", "wb") as data:
#     pickle.dump(user, data)

# with open("Name.p", "rb") as data:
#     user = pickle.load(data)
#
# print(user)
