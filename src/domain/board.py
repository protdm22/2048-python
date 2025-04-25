from random import randint

from texttable import Texttable
from src.utils.next_value import Next


class Board:
    def __init__(self):
        self.__board = [[0 for _ in range(4)] for _ in range(4)]

    def __str__(self):
        board_to_print = Texttable()
        for row in self.__board:
            board_to_print.add_row(row)
        return board_to_print.draw()

    def __getitem__(self, key: tuple):
        return self.__board[key[0]][key[1]]

    def __setitem__(self, key: tuple, value):
        self.__board[key[0]][key[1]] = value
