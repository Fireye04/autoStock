import pickle


class User:
    def __init__(self, userName: str, currentFunds: int, currentStockList: [[str, int], ...]):
        self.name = userName

        self.funds = currentFunds

        #paired list [stock: str, money in stock: int]
        self.stocks = currentStockList

        #just the strs
        self.plainStocks = []

        for i in range(len(self.stocks)):
            self.plainStocks.append(self.stocks[i][0])

        # calculates funds in stock
        self.fundsInStock = 0

        # iterates over stockList and adds all stock values
        for i in range(len(self.stocks)):
            self.fundsInStock += self.stocks[i][1]

    def setFunds(self, amount: int, increment: bool):
        if increment:
            self.funds += amount
        else:
            self.funds = amount

    def __str__(self):
        return f"{self.name}'s Stock Profile- \n~~~\nNet Worth- ${self.funds + self.fundsInStock} \n" \
               f"Funds- ${self.funds} \nMoney In Stocks- ${self.fundsInStock} \nStocks- {self.plainStocks} \n" \
               f"Paired Stocks- {self.stocks}"


# uncomment this to change the acting user
#
user = User("Name", 100_000, [[]])
with open(user.name + ".p", "wb") as data:
    pickle.dump(user, data)

with open("Name.p", "rb") as data:
    user = pickle.load(data)

print(user)
