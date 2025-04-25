from src.domain.board import Board
from src.service.game_logic import GameLogic


class UI:
    def __init__(self):
        self.__service = GameLogic()

    def run(self):
        while True:
            self.print_board()
            option = input("Next move: ")
            if option == "up":
                self.__service.move_up()
            if option == "0":
                break

    def print_board(self):
        print(self.__service.board)
