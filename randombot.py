""" This is a subclass of the Player class which represents a bot.
    It chooses a column randomly from all possible (unfilled) columns
    through overriding the choose_column(board) method.
"""
from connect4 import *

class RandomBot():
    def __init__(self):
        pass

    def choose_column(self, board: List[List[BoardValue]]) -> int:
        possible_column = []
        for i in range(7):
            if board[0][i] == BoardValue.EMPTY:
                possible_column.append(i)
        if len(possible_column) == 0:
            raise ValueError
        return random.choice(possible_column)
