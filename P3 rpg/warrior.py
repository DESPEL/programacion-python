from character import Character
from renderable import Renderable

from image_loader import load_console_sprite
from gui import GUI, Point
from copy import deepcopy

WARRIOR_IMAGE = load_console_sprite("sprites/warrior.png")


class Warrior(Character, Renderable):
    def __init__(self, position):
        Character.__init__(self, 10, 5, 2, 1, {
            "espadazo": 3.5,
            "golpe": 2,
            "patada": 1
        })
        self.position = Point(position.x, position.y + 1)
        Renderable.__init__(self, deepcopy(WARRIOR_IMAGE), self.position)

    def print_hp(self):
        hp_bar = self.get_hp_bar()
        pos = Point(self.position.x, self.position.y - 1)
        GUI.print(pos, hp_bar)


if __name__ == "__main__":
    from gui import Point
    from colorama import init

    init(True)

    warrior = Warrior(Point(0, 0))
    warrior.print_hp()
    print(warrior)
