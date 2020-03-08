from gui import Point, GUI


class Renderable:
    def __init__(self, image, position):
        self.image = image
        self.position = position

    def print(self):
        GUI.print(self.position, self.image)

    def reflect(self):
        result = []
        for row in self.image.data:
            result.append(row[::-1])
        self.image.data = result

    def __repr__(self):
        self.print()
        return ""
