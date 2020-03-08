import colorama
from colorama import Fore, Back, Style
import os
colorama.init()

WIDTH = 120
HEIGHT = 40


def move(y, x):
    print("\033[%d;%dH" % (y, x), end="")


class Console:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT

        self.buffer = [
                [[Fore.WHITE, Back.BLACK, " "] for _ in range(WIDTH)]
                for _ in range(HEIGHT)
        ]

    def print_at(self, y, x, string, fore=Fore.WHITE, back=Back.BLACK):
        idx = x
        for c in string:
            if idx == self.width:
                self.idx = x
                y += 1
            if y == self.height:
                break
            move(y, idx)
            print(fore + back + c)
            self.buffer[y][idx] = [fore, back, c]
            idx += 1

    def force_update(self):
        os.system('cls')
        for r in self.buffer:
            for v in r:
                print(v[0] + v[1] + v[2], end="")
            print("\n", end="")

    def clear_buffer(self):
        self.buffer = [[
            [Fore.WHITE, Back.BLACK, " "] for _ in range(WIDTH)]
            for _ in range(HEIGHT)
        ]


os.system("cls")
console = Console()

if __name__ == "__main__":
    console.print_at(
            10, 10,
            "TESASDFASDLGASDBJLKASDNBKLSDLKVKDLSFKLAJSDFLKAJSKDLFJALSKDFKLT",
            Fore.BLUE)
