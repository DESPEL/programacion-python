from copy import deepcopy

from character import Character
from renderable import Renderable

from image_loader import load_console_sprite
from gui import GUI, Point

ARCHER_IMAGE = load_console_sprite("sprites/archer.png")


class Archer(Character, Renderable):
    def __init__(self, position):
        Character.__init__(self, 10, 2, 3, 5, {
            "flecha": 3,
            "golpe": 2,
            "patada": 1
        })
        self.position = Point(position.x, position.y + 1)
        Renderable.__init__(self, deepcopy(ARCHER_IMAGE), self.position)

    def print_hp(self):
        hp_bar = self.get_hp_bar()
        pos = Point(self.position.x, self.position.y - 1)
        GUI.print(pos, hp_bar)
