from colorama import init

init()


class MoveCursor:
    def __call__(self, y, x):
        print("\033[%d;%dH" % (y, x), end="")


move = MoveCursor()
