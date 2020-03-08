from functools import reduce
from random import shuffle

from card import (
    Card,
    NAMES,
    SUITS
)


class Deck:
    def __init__(self, amount=4):
        self.amount = amount
        self.create_deck()

    def create_deck(self):
        self.deck = [[Card(v, n) for v in NAMES] for n in SUITS] * self.amount
        self.deck = reduce(lambda x, y: x + y, self.deck)
        shuffle(self.deck)

    def pop(self):
        return self.deck.pop()
