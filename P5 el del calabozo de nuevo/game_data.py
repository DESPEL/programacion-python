from db import DB


class GameState:
    def __init__(self):
        self.state = DB("game_state.csv")
        self.data = self.state.data[0]

    def save(self):
        self.state.save()


if __name__ == "__main__":
    test = GameState()
    print(test.data)
