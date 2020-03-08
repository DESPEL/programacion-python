from colorama import Fore

SUITS = ["♥", "♦", "♣", "♠"]
NAMES = [
    "A", "2", "3", "4",
    "5", "6", "7", "8",
    "9", "10", "J", "Q", "K"
]

RAW_VALUES = [x if x < 10 else 10 for x in range(1, 14)]
VALUES = {n: v for (n, v) in zip(NAMES, RAW_VALUES)}


class Card:
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.value = VALUES[name]

    def is_red(self):
        return self.suit == SUITS[0] or self.suit == SUITS[1]

    def __repr__(self):
        color = Fore.RED if self.is_red else Fore.WHITE
        return f"{color}{self.name}{self.suit}"
