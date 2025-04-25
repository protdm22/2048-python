from src.ui.ui import UI


class Game:
    def __init__(self):
        self.__ui = UI()

    def start(self):
        self.__ui.run()


if __name__ == "__main__":
    game = Game()
    game.start()
