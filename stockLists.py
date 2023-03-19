from temp import nasdaq
from temp import sAndP500
from temp import dowJones
import pickle

def choiceCalc(pairs):
    Final = []
    for i in range(len(pairs)):
        for j in range(pairs[i][1]):
            Final.append(pairs[i][0])
    return Final


def multiplierCalc(weights, multiplier):
    Multiplier = []

    for i in range(len(weights)):
        Multiplier.append(round(weights[i] * multiplier))

    return Multiplier


def pairCalc(stocks, weights):
    pairs = []
    for i in range(len(stocks)):
        pairs.append([stocks[i], weights[i]])
    return pairs


class StockList:
    def __init__(self, listName, listStocks, listWeights, listMultiplier=10):
        self.name = listName
        self.stocks = listStocks
        self.weights = listWeights
        self.pairs = pairCalc(self.stocks, self.weights)

        self.stockMultiplier = listMultiplier
        self.multipliers = multiplierCalc(self.weights, self.stockMultiplier)
        self.choicePairs = pairCalc(self.stocks, self.multipliers)
        self.choice = choiceCalc(self.choicePairs)

    def __str__(self):
        return f"{self.name} \n~~~\nPairs- {self.pairs} \nStocks- {self.stocks} \nWeights- {self.weights} \n" \
               f"Multipliers- {self.multipliers}\n"


nas = StockList("Nasdaq", nasdaq.stock, nasdaq.weights)
dow = StockList("Dow Jones", dowJones.stock, dowJones.weights)
sp5 = StockList("S&P 500", sAndP500.stock, sAndP500.weights, 100)

sList = [nas, dow, sp5]

with open("stockRepo.p", "wb") as data:
    pickle.dump(sList, data)

with open("stockRepo.p", "rb") as data:
    sList2 = pickle.load(data)

for i in sList2:
    print(i)
