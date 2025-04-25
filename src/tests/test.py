from src.domain.board import Board
from src.service.game_logic import GameLogic


logic = GameLogic()
for i in range(4):
    for j in range(4):
        logic.board[(i, j)] = 0
logic.board[(0,0)] = 4
logic.board[(0,1)] = 4
logic.board[(0,2)] = 2
logic.board[(0,3)] = 4
logic.board[(1,1)] = 2
logic.board[(1,3)] = 2

logic.move_up()
# print(logic.board)
