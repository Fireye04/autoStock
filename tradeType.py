from enum import Enum, auto


class TradeType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    SHORT = "SELL SHORT"
    COVER = "BUY TO COVER"
