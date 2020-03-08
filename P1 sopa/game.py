from os import system
from colorama import Fore, Back

import keyboard
from console import console

from board import Board
from size import Size
from point2 import Point2

import time

DELTAS = [[0, -1], [-1, -1], [-1, 0],
          [-1, 1], [0, 1], [1, 1],
          [1, 0], [1, -1]]
KEYS = "wqazxcde"

SPACE = 2


class Game:
    def __init__(self, size, words):
        w, h = size
        self.size = size
        self.board = Board(size, words)
        self.found = [[False for _ in range(h)] for _ in range(w)]
        self.found_idx = []
        self.selected = []
        self.pos = Point2(0, 0)

        self.offset_x = 3
        self.offset_y = 3

        self.cursor_color = Back.GREEN
        self.s_color = Back.LIGHTBLUE_EX

        for key, [dx, dy] in zip(KEYS, DELTAS):
            mov_cursor = self.gen_move_cursor(Point2(dx, dy))
            sel_cursor = self.gen_select_cursor(Point2(dx, dy))
            keyboard.add_hotkey(key, mov_cursor)
            keyboard.add_hotkey('alt+' + key, sel_cursor)

    def print_new_pos(self, delta):
        x, y = self.pos
        dx, dy = delta
        px = self.offset_x + SPACE*x
        py = self.offset_y + SPACE*y
        fore = Fore.RED if self.found[y-dy][x-dx] else Fore.WHITE
        console.print_at(
            py-SPACE*dy, px-SPACE*dx, self.board.board[y-dy][x-dx], fore=fore
        )

        px = self.offset_x + SPACE*x
        py = self.offset_y + SPACE*y
        fore = Fore.RED if self.found[y][x] else Fore.WHITE
        console.print_at(
            py, px, self.board.board[y][x], back=self.cursor_color, fore=fore
        )

        for x, y in self.selected:
            px = self.offset_x + SPACE*x
            py = self.offset_y + SPACE*y
            console.print_at(py, px, self.board.board[y][x], back=self.s_color)

    def make_word_from_idx(self, idxs):
        word = ''
        for x, y in idxs:
            word += (self.board.board[y][x])
        return word

    def is_word_selected(self):
        word = self.make_word_from_idx(self.selected)
        return word in self.board.words or word[::-1] in self.board.words

    def get_word_idx(self, word):
        try:
            return self.board.words.index(word)
        except:
            try:
                return self.board.words.index(word[::-1])
            except:
                return None

    def move_cursor(self, delta, from_selection=False):
        ox, oy = self.pos
        len_ = len(self.board.board[0])
        x = ox + delta.x if 0 <= ox + delta.x <= len_-1 else ox
        y = oy + delta.y if 0 <= oy + delta.y <= len_-1 else oy
        self.pos = Point2(x, y)
        self.print_new_pos((x-ox, y-oy))

        word_selected = self.is_word_selected()
        if not from_selection and not word_selected:
            self.clear_selected()
        if word_selected:
            word = self.make_word_from_idx(self.selected)
            idx = self.get_word_idx(word)
            for x, y in self.selected:
                self.found[y][x] = True
            self.found_idx.append(idx)
            self.clear_selected()
            self.print_board()
            if len(self.found_idx) == len(self.board.words):
                self.end_game()

    def gen_move_cursor(self, delta):
        def move_cursor():
            self.move_cursor(delta)
        return move_cursor

    def clear_selected(self):
        for x, y in self.selected:
            px = self.offset_x + SPACE*x
            py = self.offset_y + SPACE*y
            console.print_at(py, px, self.board.board[y][x], back=Back.BLACK)
        self.selected.clear()

    def verify_select(self):
        if len(self.selected) <= 1:
            return True
        sel = self.selected
        dx = sel[1].x - sel[0].x
        dy = sel[1].y - sel[0].y
        lx = sel[0].x
        ly = sel[0].y
        for x, y in sel[1:]:
            if x - lx != dx or y - ly != dy:
                self.clear_selected()
                return False
            lx = x
            ly = y
        return True

    def gen_select_cursor(self, delta):
        def select_cursor():
            self.selected.append(self.pos)
            self.verify_select()
            self.move_cursor(delta, True)
        return select_cursor

    def print_board(self):
        console.print_at(1, 1, "Sopa de letras")
        w, h = self.size
        for i in range(w):
            for j in range(h):
                px, py = self.pos
                color = Back.GREEN if j == px and i == py else None
                c = self.board.board[i][j]
                fore = Fore.RED if self.found[i][j] else Fore.WHITE
                if color:
                    console.print_at(
                        self.offset_y+i*SPACE,
                        self.offset_x+j*SPACE, c,
                        fore=fore,
                        back=color
                    )
                else:
                    console.print_at(
                        self.offset_y+i*SPACE,
                        self.offset_x+j*SPACE, c,
                        fore=fore
                    )
        self.print_controls()
        self.print_words()

    def print_words(self):
        for i, word in enumerate(self.board.words, 1):
            if i-1 in self.found_idx:
                console.print_at(i+2, 100, f"{i}) {word}", fore=Fore.GREEN)
            else:
                console.print_at(i+2, 100, f"{i}) {word}")

    def print_controls(self):
        console.print_at(4, 60, "Controles:")
        console.print_at(5, 60, "w - Cursor arriba")
        console.print_at(6, 60, "q - Cursor arriba-izquierda")
        console.print_at(7, 60, "a - Cursor izquierda")
        console.print_at(8, 60, "z - Cursor abajo-izquierda")
        console.print_at(9, 60, "x - Cursor abajo")
        console.print_at(10, 60, "c - Cursor abajo-derecha")
        console.print_at(11, 60, "d - Cursor derecha")
        console.print_at(12, 60, "e - Cursor arriba-derecha")

        console.print_at(14, 60, "alt+direccion - Seleccionar")
        console.print_at(15, 60, "Moverse normal para terminar selección")

    def end_game(self):
        system("cls")
        console.print_at(
            1, 1,
            "Completaste la sopa de letras", fore=Fore.YELLOW)

    @staticmethod
    def start():
        console.print_at(1, 1, "Creando tablero")
        console.print_at(2, 1, "Toma entre 5 y 20 segundos")
        test = Game(Size(5, 5), 5)

        console.clear_buffer()
        console.force_update()
        test.print_board()

        time.sleep(500000.0)


if __name__ == "__main__":
    console.print_at(1, 1, "Creando tablero")
    console.print_at(2, 1, "Toma entre 5 y 20 segundos")
    test = Game(Size(14, 28), 25)

    console.clear_buffer()
    console.force_update()
    test.print_board()

    time.sleep(500000.0)
