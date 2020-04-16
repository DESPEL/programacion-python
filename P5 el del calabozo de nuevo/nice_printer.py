from move_cursor import move


class CoordPrinter:
    def __call__(self, pos, text):
        x, y = pos
        for row in text:
            move(y, x)
            print(row)
            y += 1


nice_print = CoordPrinter()
