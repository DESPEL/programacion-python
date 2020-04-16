from tile import TileMap
from player import Player

import colorama
from colorama import Fore


class Game:
    def __init__(self):
        self.tilemap = TileMap.generate_left_right()

    def render_tilemap(self):
        self.tilemap["left"].render()
        self.tilemap["center"].render()
        self.tilemap["right"].render()

    def play(self):
        self.p1 = Player(self.tilemap["left"], Fore.BLUE)
        self.p2 = Player(self.tilemap["right"], Fore.RED)

    def pause(self):
        pass


if __name__ == "__main__":
    test = Game()
    test.play()
    test.render_tilemap()
    test.p1.turn()
    test.render_tilemap()
