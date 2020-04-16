import time

import colorama

from random import choice

from lib import safe_input, clear_screen

from wizard import Wizard
from archer import Archer
from warrior import Warrior

from gui import Point, GUI, Image

colorama.init(True)


class Game:
    def __init__(self):
        self.character_constructor = {
            "Mago": Wizard,
            "Arquero": Archer,
            "Guerrero": Warrior
        }
        self.character_stat_strings = [
            " HP: 15 STR: 2 DEF: 3 EV: 4",
            " HP: 10 STR: 2 DEF: 3 EV: 5",
            " HP: 10 STR: 5 DEF: 2 EV: 1"
        ]
        self.character_types = list(self.character_constructor.keys())

    def run(self):
        self.mode = self._get_game_mode()
        if self.mode == "solo":
            self._run_solo()
        else:
            self._run_multi()

    def _run_solo(self):
        self._create_players_solo()

        while (self.computer.is_alive() and self.player1.is_alive()):
            self._print_gui()
            print("Turno Jugador 1")
            self._player_turn(self.player1, self.computer)
            self._computer_turn()

        self._print_winner()

    def _run_multi(self):
        self._create_players_multi()

        while (self.player1.is_alive() and self.player2.is_alive()):
            self._print_gui()
            print("Turno Jugador 1")
            self._player_turn(self.player1, self.player2)
            if not self.player2.is_alive():
                break
            self._print_gui()
            print("Turno Jugador 2")
            self._player_turn(self.player2, self.player1)

        self._print_winner()

    def _print_gui(self):
        clear_screen()
        self.player1.print_hp()
        print(self.player1)

        if self.mode == "solo":
            self.computer.print_hp()
            print(self.computer)
        else:
            self.player2.print_hp()
            print(self.player2)

    def _print_winner(self):
        if self.player1.is_alive():
            print("Ha ganado el jugador 1")
        else:
            print("Ha ganado el jugador 2")

    def _computer_turn(self):
        attack_name = choice(list(self.computer.attacks.keys()))
        print(f"La computadora te ha atacado con: {attack_name}")
        self.computer.attack(self.player1, attack_name)
        time.sleep(0.3)

    def _player_turn(self, from_player, to_player):
        attack_name = self._get_player_attack_name(from_player)
        from_player.attack(to_player, attack_name)

    def _print_player_attacks(self, player):
        for idx, (attack, power) in enumerate(player.attacks.items(), 1):
            print(f"{idx}) {attack}: {power} poder")

    def _get_player_attack_name(self, player):
        print("Seleccione el ataque que desea utilizar")
        self._print_player_attacks(player)
        attack_id = safe_input(
            lambda x: x >= 1 and x <= len(player.attacks),
            "Ingrese el número de ataque que desea utilizar: ",
            errmsg="Ese ataque no es válido",
            type_=int
        )
        return list(player.attacks.keys())[attack_id - 1]

    def _create_players_solo(self):
        player1_type = self._get_player_character_type()
        self.player1 = self.character_constructor[player1_type](Point(2, 0))

        computer_type = choice(self.character_types)
        self.computer = self.character_constructor[computer_type](Point(60, 0))
        self.computer.reflect()

    def _create_players_multi(self):
        player1_type = self._get_player_character_type()
        self.player1 = self.character_constructor[player1_type](Point(2, 0))

        player2_type = self._get_player_character_type()
        self.player2 = self.character_constructor[player2_type](Point(60, 0))
        self.player2.reflect()

    def _get_player_character_type(self):
        print("Seleccione su tipo de personaje:")
        for idx, (character, stats) in enumerate(
            zip(self.character_types, self.character_stat_strings), 1
        ):
            print(f"{idx}) {character}, {stats}")

        character_type = safe_input(
            lambda x: x >= 1 and x <= len(self.character_types),
            "Ingrese la opción (número):",
            errmsg="Tipo de personaje no válido",
            type_=int
        )
        return self.character_types[character_type - 1]

    def _get_game_mode(self):
        print("Bienvenido al juego RPG")
        print("Seleccione el modo de juego:")
        print("1) Solo")
        print("2) Multijugador")
        mode = safe_input(
            lambda x: x >= 1 and x <= 2,
            "Ingrese la opción (número):",
            errmsg="Modo de juego no válido",
            type_=int
        )
        return "solo" if mode == 1 else "multi"


test = Game()
test.run()
