from colorama import Fore
import colorama

from utils import typed_input, safe_input
from deck import Deck
from player import Dealer, Player
from hand import Hand

from utils import clear_screen

colorama.init(True)


class Game:
    def __init__(self):
        self.init()

        self._create_players()

    def _create_players(self):
        self.dealer = Dealer()

        name = input("Ingrese su nombre: ")
        money = typed_input(
            int,
            "Ingrese la cantidad de dinero que tiene: ",
            f"{Fore.RED}Error: Ingrese una cantidad válida"
        )
        self.player = Player(name, money)

    def bet(self):
        print(f"Tienes {self.player.money} dinero")
        bet_value = safe_input(
            lambda x: x > 0 and x <= self.player.money,
            "Ingrese la cantidad a apostar: ",
            f"{Fore.RED}Error: Ingrese una cantidad válida",
            type_=int
        )
        self.player.hands.append(Hand([], bet_value))
        self.player.money -= bet_value

    def init(self):
        self.deck = Deck()
        self.round = 0
        self.ended = False

    def run(self):
        self.init()
        self.bet()
        keep = "1"
        while keep == "1":
            self.play_game()
            keep = input("Ingrese 1 para jugar de nuevo:")
            if keep != "1":
                break
            self.player = Player(self.player.name, self.player.money)
            self.init()

    def play_game(self):
        while not self.player.has_ended() and not self.round > 3:
            if self.dealer.get_max_points() < 17:
                self.dealer.add(self.deck.pop())
            for i in range(self.player.get_num_hands()):
                self.player.current = i
                self.turn_hand()
            self.player.has_ended()
            self.round += 1
        self.show_wins()

    def turn_hand(self):
        self.print_hands(self.player.current)
        if self.player.is_current_complete():
            return
        if self.player.can_split_current():
            self.split()
        if self.dealer.can_buy_insurance():
            self.buy_insurance()
        opt = self.get_opt()
        if opt == 1:
            self.player.double_current_bet()
        if opt == 2:
            self.player.add_card_current(self.deck.pop())
        if opt == 3:
            self.player.complete_current()
        clear_screen()

    def get_opt(self):
        print("1) Doblar apuesta")
        print("2) Pedir otra carta")
        print("3) Plantarse")
        return safe_input(
            lambda x: x >= 1 and x <= 3,
            "Ingrese el número de la opción",
            f"{Fore.RED}Error: Ingrese una opción válida",
            type_=int
        )

    def buy_insurance(self):
        v = input("Ingrese 1 si desea comprar un seguro: ")
        if v != 1:
            return
        self.player.buy_insurance()

    def split(self):
        v = input("Ingrese 1 si desea hacer un split: ")
        if v != "1":
            return
        self.player.split()

    def print_hands(self, current, all_=False):
        self._print_dealer(all_)
        self.player.current = current
        self._print_player_hand()

    def _print_dealer(self, all_):
        print(f"{self.dealer.name}: ")
        if all_:
            self.dealer.print_all()
        else:
            self.dealer.print_hand()

    def _print_player_hand(self):

        print(f"{self.player.name}, mano {self.player.current+1}:")
        self.player.print_current_hand()
        print(f"Puntos: {self.player.get_max_current_points()}")
        print(f"Dinero: {self.player.money}")
        print(f"Dinero apostado en mano: {self.player.get_current_bet()}")

    def show_wins(self):
        for i in range(self.player.get_num_hands()):
            self.player.current = i

            dealer_points = self.dealer.hand.get_max_points()
            player_points = self.player.get_max_current_points()
            hand = self.player.hands[self.player.current]

            if self.player.has_current_insurance():
                self._show_insurance_win()
            if self.player.is_current_surrended():
                self._show_surrender_win()
            elif dealer_points == player_points:
                self._show_tie()
            elif player_points > 21 or dealer_points > player_points:
                self._show_p()
            elif player_points == 21 and len(hand) == 2:
                self._show_blackjack_win()
            else:
                self._print_win()
        input("Ingrese algo para continuar")
        clear_screen()

    def _print_win(self):
        print("Ganaste, recibes 1 a 1")
        self.player.money += self.player.get_current_bet()*2
        print(f"Dinero: {self.player.money}")

    def _show_blackjack_win(self):
        print("Ganaste por blackjack, recibes 3 a 2")
        self.player.money += self.player.get_current_bet()/2*5
        print(f"Dinero: {self.player.money}")

    def _show_p(self):
        print("Perdiste:")
        print(f"Dinero: {self.player.money}")

    def _show_tie(self):
        print("Empate:")
        self.player.money += self.player.get_current_bet()
        print(f"Dinero: {self.player.money}")

    def _show_surrender_win(self):
        print("Perdiste la mitad del dinero de la apuesta")
        self.player.money += self.player.get_current_bet()/2
        print(f"Dinero: {self.player.money}")

    def _show_insurance_win(self):
        dealer_21 = self.dealer.hand.get_max_points() == 1
        dealer_blackjack = len(self.dealer.hand.cards) == 2 and dealer_21

        if dealer_blackjack:
            print("Ganaste el dinero del seguro")
            self.player.money += (self.player.get_current_bet()/2)*3
            print(f"Dinero: {self.player.money}")
        else:
            print("Perdiste el dinero del seguro")


if __name__ == "__main__":
    juego = Game()
    juego.run()
