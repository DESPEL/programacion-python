import colorama
from colorama import Fore
from os import system
from random import randint

from move_cursor import move
from nice_printer import nice_print

colorama.init()

system("cls")


class TileMap:
    def __init__(self, tiles):
        self.tiles = tiles

    def render(self):
        for row in self.tiles:
            for tile in row:
                tile.render()

    @staticmethod
    def generate_left_right():

        left = TileMap(
            [
                [Tile((2, 2)), ],
                [Tile((7, 2)), Tile((7, 5))],
                [Tile((12, 2)), Tile((12, 5)), Tile((12, 8))],
                [Tile((17, 2)), Tile((17, 5)), Tile((17, 8))],
                [Tile((22, 2)), Tile((22, 5)), Tile((22, 8))],
            ]
        )

        center = Tile((27, 5))

        right = TileMap(
            [
                [Tile((52, 2)), ],
                [Tile((47, 2)), Tile((47, 5))],
                [Tile((42, 2)), Tile((42, 5)), Tile((42, 8))],
                [Tile((37, 2)), Tile((37, 5)), Tile((37, 8))],
                [Tile((32, 2)), Tile((32, 5)), Tile((32, 8))],
            ]
        )
        ven_row = randint(1, len(left.tiles)-1)
        ven_col = randint(0, len(left.tiles[ven_row])-1)

        left.tiles[ven_row][ven_col].venomous = True
        right.tiles[ven_row][ven_col].venomous = True

        return {
            "left": left,
            "center": center,
            "right": right
        }


class Tile:
    def __init__(self, position, value=None, venomous=False):
        self.value = value if value else randint(2, 20)
        self.position = position
        self.venomous = venomous
        self.has_player = True
        self.color = Fore.YELLOW
        self.opened = False

    def render(self):
        x, y = self.position
        move(y, x)
        t = " " + str(self.value) if self.value < 10 else self.value
        t = t if self.opened else "xx"
        print(self.has_player)
        if self.venomous:
            print(Fore.GREEN)
        if self.has_player:
            print(self.color)
        nice_print(self.position, [
            "+--+",
            f"|{t}|",
            "+--+",
        ])
        print(Fore.WHITE)


if __name__ == "__main__":
    test = Tile((22, 5), 10)
    test.render()

    tilemap_test_l = TileMap(
        [
            [Tile((2, 2)), ],
            [Tile((7, 2), venomous=True), Tile((7, 5)), Tile((7, 8))],
            [Tile((12, 2)), Tile((12, 5)), Tile((12, 8))],
            [Tile((17, 2)), Tile((17, 5)), Tile((17, 8))],
        ]
    )
    tilemap_test_l.render()

    tilemap_test_r = TileMap(
        [
            [Tile((27, 2)), Tile((27, 5)), Tile((27, 8))],
            [Tile((32, 2), venomous=True), Tile((32, 5)), Tile((32, 8))],
            [Tile((37, 2)), Tile((37, 5)), Tile((37, 8))],
            [Tile((42, 2)), ],
        ]
    )
    tilemap_test_r.render()
