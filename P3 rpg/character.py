import abc
from colorama import Back

from utils import random_event
from gui import Image

from character_interface import CharacterInterface


@CharacterInterface.register
class Character:
    def __init__(self, hp, power, defense, evasion_rate, attacks):
        self.max_hp = hp * 5
        self.hp = self.max_hp
        self.power = power
        self.defense = defense
        self.evasion_rate = evasion_rate * 10
        self.attacks = attacks

    def attack(self, objective, attack_name):
        power = self.attacks[attack_name] * self.power / 5
        objective.defend(power)

    def defend(self, attack):
        if random_event(self.evasion_rate / 100):
            print("EVADED")
            return
        self.hp -= attack / (self.defense / 10)

    def is_alive(self):
        return self.hp > 0

    def get_hp_bar(self):
        hp_parts = int(self.hp / self.max_hp * 20)

        left = Back.RED + "  " * hp_parts
        lost = Back.WHITE + "  " * (20 - hp_parts)
        hp_bar = f"HP:{left}{lost}"

        return Image([hp_bar, ])


assert(issubclass(Character, CharacterInterface))
