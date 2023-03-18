
class StockList:
    def __init__(self, listStocks, listWeights, listMultiplier=.001):
        self.stocks = listStocks
        self.weights = listWeights
        self.pairs = self.pairCalc(self.stocks, self.weights)

        self.stockMultiplier = listMultiplier
        self.multipliers = self.multiplierCalc(self.weights, self.stockMultiplier)
        self.choicePairs = self.pairCalc(self.stocks, self.multipliers)
        self.choice = self.choiceCalc(self.choicePairs)

    def choiceCalc(self, pairs):
        Final = []
        for i in range(len(pairs)):
            for j in range(pairs[i][1]):
                Final.append(pairs[i][0])
        return Final

    def multiplierCalc(self, weights, multiplier):
        Multiplier = []

        for i in range(len(weights)):
            Multiplier.append(round(weights[i] * multiplier))

        return Multiplier

    def pairCalc(self, stocks, weights):
        pairs = []
        for i in range(len(stocks)):
            pairs.append([stocks[i], weights[i]])
        return pairs
