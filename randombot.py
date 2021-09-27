""" This example is a subclass of Player.
    It choose a column randomly from all possible (unfilled) columns
    by override choose_column(board) method
"""
from connect4 import *

class RandomBot(Player):
    def choose_column(self, board: List[List[BoardValue]]) -> int:
        possible_column = []
        for i in range(7):
            if board[0][i] == BoardValue.EMPTY:
                possible_column.append(i)
        if len(possible_column) == 0:
            raise ValueError
        return random.choice(possible_column)
