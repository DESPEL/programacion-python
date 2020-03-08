class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __iter__(self):
        return (prop for prop in [self.width, self.height])
