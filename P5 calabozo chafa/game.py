import os
import colorama
from colorama import Fore
from random import randint
from db import DB


colorama.init()
os.system("cls")


def nice_print(pos, text):
    x, y = pos
    for row in text:
        move(y, x)
        print(row)
        y += 1


def move(y, x):
    print("\033[%d;%dH" % (y+1, x+1), end="")


def pause(game):
    os.system("cls")
    print("Juego pausado")
    print("1) Continuar")
    print("2) Salir y guardar")
    print("3) Salir")

    v = input("Ingrese una opción: ")
    if v == "1":
        return False
    if v == "2":
        a = DB("game.csv")
        a.data[0] = game
        a.save()
    return True


class Player:
    def __init__(self, color):
        self.color = color
        self.pos = (0, 0)
        self.poisoned = False
        self.points = 0


class Tile:
    def __init__(self, pos, value=None):
        self.value = value if value else randint(2, 20)
        self.opened = False
        self.pos = pos
        self.venomous = False
        self.color = Fore.WHITE
        self.has_player = False

    def render(self):
        x, y = self.pos
        move(y, x)
        t = " " + str(self.value) if self.value < 10 else self.value
        t = t if self.opened else "xx"
        if self.venomous and self.opened:
            print(Fore.GREEN)
        if self.has_player:
            print(self.color)
        nice_print(self.pos, [
            "+--+",
            f"|{t}|",
            "+--+",
        ])
        print(Fore.WHITE)


class Board:
    def __init__(self, tiles):
        self.tiles = tiles

    def render(self):
        for row in self.tiles:
            for tile in row:
                tile.render()

    @staticmethod
    def gen_board():
        left = Board(
            [
                [Tile((2, 2)), ],
                [Tile((7, 2)), Tile((7, 5))],
                [Tile((12, 2)), Tile((12, 5)), Tile((12, 8))],
                [Tile((17, 2)), Tile((17, 5)), Tile((17, 8))],
                [Tile((22, 2)), Tile((22, 5)), Tile((22, 8))],
            ]
        )

        center = Tile((27, 5))

        right = Board(
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

        ven_row = randint(1, len(left.tiles)-1)
        ven_col = randint(0, len(left.tiles[ven_row])-1)

        left.tiles[ven_row][ven_col].opened = True
        right.tiles[ven_row][ven_col].opened = True

        ven_row = randint(1, len(left.tiles)-1)
        ven_col = randint(0, len(left.tiles[ven_row])-1)

        left.tiles[ven_row][ven_col].opened = True
        right.tiles[ven_row][ven_col].opened = True

        return {
            "left": left,
            "center": center,
            "right": right
        }


class Game:
    def __init__(self):
        self.p1 = Player(Fore.BLUE)
        self.p2 = Player(Fore.RED)

        tmp_board = Board.gen_board()
        self.left = tmp_board["left"]
        self.center = tmp_board["center"]
        self.right = tmp_board["right"]

        self.left.tiles[0][0].color = Fore.BLUE
        self.left.tiles[0][0].has_player = True
        self.right.tiles[0][0].color = Fore.RED
        self.right.tiles[0][0].has_player = True

        self.remaining = 4

    def start(self):
        for _ in range(self.remaining):
            os.system("cls")
            self.left.render()
            self.right.render()
            self.center.render()
            move(11, 0)
            print(f"{self.p1.color}Puntos: {self.p1.points}")
            self.turn(self.p1, self.left)
            os.system("cls")

            self.left.render()
            self.right.render()
            self.center.render()
            move(11, 0)
            print(f"{self.p2.color}Puntos: {self.p2.points}")
            self.turn(self.p2, self.right)
            os.system("cls")

            self.left.render()
            self.right.render()
            self.center.render()
            self.remaining -= 1

            move(11, 0)
            if input("ingrese p si desea pausar el juego: ") == "p":
                b = pause(self)
                if b:
                    return
        os.system("cls")
        p1pts = self.p1.points if not self.p1.poisoned else self.p1.points / 2
        p2pts = self.p2.points if not self.p2.poisoned else self.p2.points / 2

        if (p1pts > p2pts):
            print("El jugador 1 ha ganado")
        if (p1pts < p2pts):
            print("El jugador 2 ha ganado")
        if (p1pts == p2pts):
            print("Ha sido un empate")

        a = DB("game.csv")
        a.data[0] = Game()
        a.save()

    def turn(self, player, tilemap):
        print(f"Turno de: {player.color}Jugador{Fore.WHITE}:")
        x, y = player.pos
        if y+1 < len(tilemap.tiles[x+1]):
            print("1) Abajo")
        if y >= 1:
            print("2) Arriba")
        print("3) Enfrente")

        direction = int(input("Ingrese el numero de movimiento: "))

        tilemap.tiles[x][y].has_player = False

        x += 1
        if direction == 1:
            y += 1
        if direction == 2:
            y -= 1
        player.pos = (x, y)

        tilemap.tiles[x][y].color = player.color
        tilemap.tiles[x][y].has_player = True
        tilemap.tiles[x][y].opened = True
        player.points += tilemap.tiles[x][y].value
        player.poisoned |= tilemap.tiles[x][y].venomous


b = DB("game.csv")


print("Bienvenido al juego de los bloques")
print("Elija una opción")
print("1) Nuevo juego")
print("2) Continuar")

v = input("Elija una opción")

os.system("cls")
if v == "1":
    b.data[0] = Game()
    b.data[0].start()
if v == "2":
    b.data[0].start()
