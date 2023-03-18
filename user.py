import pickle


class User:
    def __init__(self, userName: str, currentFunds: int):
        self.name = userName

        self.funds = currentFunds

        self.stockList = [[]]


# uncomment this to change the acting user
#
user = User("Kai", 100_000)
with open("user.p", "wb") as data:
    pickle.dump(user, data)


with open("user.p", "rb") as data:
    user = pickle.load(data)
