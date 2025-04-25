import copy
from random import randint

from src.domain.board import Board
from src.utils.next_value import Next


class GameLogic:
    def __init__(self):
        self.__board = Board()
        self.__initialize_board()

    @property
    def board(self):
        return self.__board

    def __initialize_board(self):
        x1, y1 = randint(0, 3), randint(0, 3)
        self.__board[(x1, y1)] = Next.next_value()

        x2, y2 = randint(0, 3), randint(0, 3)
        while x1 == x2 and y1 == y2:
            x2, y2 = randint(0, 3), randint(0, 3)

        self.__board[(x2, y2)] = Next.next_value()

    def __next_appearance(self):
        empty_fields = []
        for row in range(4):
            for column in range(4):
                if self.__board[(row, column)] == 0:
                    empty_fields.append((row, column))
        self.__board[empty_fields[randint(0, len(empty_fields) - 1)]] = Next.next_value()

    def move_up(self):
        for column in range(4):
            non_zero = []
            for row in range(4):
                if self.__board[(row, column)] != 0:
                    non_zero.append(self.__board[(row, column)])
            for row in range(4):
                if row < len(non_zero):
                    self.__board[(row, column)] = non_zero[row]
                else:
                    self.__board[(row, column)] = 0

        print(self.__board)
        next_state = Board()

        for column in range(4):
            row = 0
            new_column = []
            while row < 3:
                if self.__board[(row, column)] == self.__board[(row + 1, column)]:
                    new_column.append(self.__board[(row, column)] * 2)
                    row += 2
                else:
                    new_column.append(self.__board[(row, column)])
                    row += 1
            if self.__board[(3, column)] != 0 and self.__board[(3, column)] != self.__board[(2, column)]:
                new_column.append(self.__board[(3, column)])

            for new_field in range(len(new_column)):
                next_state[(new_field, column)] = new_column[new_field]

        self.__board = copy.deepcopy(next_state)
        self.__next_appearance()

    def move_right(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass
