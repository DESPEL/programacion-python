from hand import Hand


class Player:
    def __init__(self, name, money):
        self.money = money
        self.name = name
        self.hands = []

        self.current = 0

    def has_insurance(self, hand_idx):
        return self.hands[hand_idx].insurance

    def has_ended(self):
        completed = sum(1 for h in self.hands if h.completed)
        if completed == 0:
            return False
        return completed == len(self.hands)

    def get_max_current_points(self):
        return self.hands[self.current].get_max_points()

    def get_current_bet(self):
        return self.hands[self.current].bet

    def enable_insurance(self, hand_idx):
        self.hands[hand_idx].insurance = True

    def get_num_hands(self):
        return len(self.hands)

    def split(self):
        n_hands = self.get_num_hands()
        card = self.player.hands.pop()
        bet_value = self.player.hands[0].bet
        self.hands = [Hand(card, bet=bet_value) for _ in range(n_hands + 1)]

    def surrender(self, hand_idx):
        self.hands[hand_idx].surrended = True
        self.hands[hand_idx].completed = True

    def buy_insurance(self):
        self.hands[hand_idx].insurance = True
        self.money -= self.hands[current].bet / 2

    def print_current_hand(self):
        self.print_hand(self.current)

    def print_hand(self, hand_idx):
        for card in self.hands[hand_idx].cards:
            print(card, end=" ")
        print()

    def has_current_insurance(self):
        return self.hands[self.current].insurance

    def can_split_current(self):
        return self.hands[self.current].can_split()

    def double_current_bet(self):
        self.money -= self.hands[self.current].bet
        self.hands[self.current].bet *= 2

    def add_card_current(self, card):
        self.hands[self.current].append(card)

    def complete_current(self):
        self.hands[self.current].completed = True

    def is_current_surrended(self):
        return self.hands[self.current].surrended

    def is_current_complete(self):
        return self.hands[self.current].completed


class Dealer:
    def __init__(self):
        self.money = 1E999
        self.name = "Dealer"
        self.hand = Hand()

    def print_hand(self, hand_idx=0):
        print(self.hand.cards[0], end=" ")
        for _ in self.hand.cards[1:]:
            print("xx", end=" ")
        print()

    def print_all(self, hand_idx=0):
        for card in self.hand:
            print(card, end=" ")
        print()

    def add(self, card):
        self.hand.append(card)

    def can_buy_insurance(self):
        return self.hand.cards[0] == 'A'

    def get_max_points(self):
        return self.hand.get_max_points()
