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

    @staticmethod
    def get_next_state(non_zero):
        result = []
        for i in range(len(non_zero) - 1):
            if non_zero[i] == non_zero[i + 1]:
                result.append(non_zero[i] * 2)
                i += 1
            else:
                result.append(non_zero[i])
        if len(non_zero) == 1:
            result.append(non_zero[0])
        else:
            if non_zero[len(non_zero) - 1] != non_zero[len(non_zero) - 2]:
                result.append(non_zero[len(non_zero) - 1])
        return result

    def enter_next_state(self, next_state):
        changed = True
        if self.__board == next_state:
            changed = False
        self.__board = copy.deepcopy(next_state)
        if changed:
            self.__next_appearance()

    def move_up(self):
        next_state = Board()
        for column in range(4):
            non_zero = []
            for row in range(4):
                if self.__board[(row, column)] != 0:
                    non_zero.append(self.__board[(row, column)])
            if len(non_zero) != 0:
                result = self.get_next_state(non_zero)
                for row in range(len(result)):
                    next_state[(row, column)] = result[row]
        self.enter_next_state(next_state)

    def move_right(self):
        pass
        # TODO

    def move_down(self):
        pass
        # TODO

    def move_left(self):
        pass
        # TODO
