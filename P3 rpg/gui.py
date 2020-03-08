from os import system
import copy


class Image:
    def __init__(self, data=["", ]):
        self.data = data


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Pixel:
    def __init__(self, color):
        self.color = color
        self.data = "  "

    def __repr__(self):
        return f"{self.color}{self.data}"


DIMENSIONS = Point(135, 45)


class GUI:
    @staticmethod
    def print(position, image):
        position = copy.copy(position)
        for row in image.data:
            GUI._move_cursor(position)
            if len(row) > 0 and type(row[0]) == Pixel:
                for pixel in row:
                    print(pixel, end="")
            else:
                print(row, end="")
            position.y += 1

    @staticmethod
    def _move_cursor(point):
        print("\033[%d;%dH" % (point.y+1, point.x+1), end="")


system("cls")
