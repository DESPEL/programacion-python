class Player:
    def __init__(self, tilemap, color):
        self.tilemap = tilemap
        self.points = 0
        self.pos = (0, 0)
        self.color = color
        self.tilemap.tiles[0][0].has_player = True
        self.tilemap.render()

    def turn(self):
        x, y = self.pos
        self.tilemap.tiles[x][y].has_player = False

        can_down = self._can_move_downwards()
        can_up = self._can_move_upwards()
        self.tilemap.render()
        if (can_down):
            print("1) Abajo")
        if (can_up):
            print("2) Arriba")
        print("3) Al frente")

        direction = input("Ingrese el numero de a donde se quiere mover: ")

        x += 1
        if direction == "1":
            y += 1
        if direction == "2":
            y -= 1

        self.pos = (x, y)

        self.tilemap.tiles[x][y].color = self.color
        self.tilemap.tiles[x][y].has_player = True

        pass

    def _can_move_downwards(self):
        x, y = self.pos
        return y + 1 < len(self.tilemap.tiles[x])

    def _can_move_upwards(self):
        _, y = self.pos
        return y >= 1
