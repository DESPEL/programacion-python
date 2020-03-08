class Hand:
    def __init__(self, cards=[], bet=0):
        self.bet = bet
        self.cards = cards
        self.insurance = False
        self.surrended = False
        self.completed = False

    def get_max_points(self):
        ones = self.count_ones()
        min_points = self.get_min_total()
        max_points = total + 10 if ones > 1 else min_points
        return max_points if max_points <= 21 else min_points

    def count_ones(self):
        return sum(x.value for x in self.cards if x.value == 1)

    def get_min_total(self):
        return sum(x.value for x in self.cards)

    def pop(self):
        return self.cards.pop()

    def append(self, card):
        self.cards.append(card)

    def can_split(self):
        if len(self.cards) < 2:
            return False
        return self.cards[0].name == self.cards[1].name
