""" This file is a example of how this API works.
    This client code is an example of connect4 between a human and a computer.
"""
from connect4 import *

# sample method used to implement a computer player
# can call this method instead of input() for a player
def choose_rand_column(board: List[List[BoardValue]]) -> int:
        possible_column = []
        for i in range(7):
            if board[0][i] == BoardValue.EMPTY:
                possible_column.append(i)
        if len(possible_column) == 0:
            raise ValueError
        return random.choice(possible_column)

# prints and formats the game board to stdout
def print_board(board: List[List[BoardValue]]) -> None:
    """You may show the board like this.
    """
    print("============================")
    for i in range(6):  # iterate 6 rows
        for j in range(7):  # iterate 7 elements in the row
            if board[i][j] == BoardValue.EMPTY:
                print("_", end=" ")
            elif board[i][j] == BoardValue.A_TOKEN:
                print("A", end=" ")
            elif board[i][j] == BoardValue.B_TOKEN:
                print("B", end=" ")
        print()
    print("============================")

if __name__ == '__main__':
    connect4 = Connect4()  # instantiate Connect4
    board = connect4.get_board()  # get board from connect4
    print_board(board)  # an empty board is shown

    game_state = connect4.get_game_state()  # get the current game state (should be GAME_CONTINUE at beginning
    while game_state == GameState.GAME_CONTINUE:  # while there is no winner, and the board is not full, the game can continue
        curr_player = connect4.get_curr_player()  # get current player for this round
        print(curr_player)
        print("enter a column value (0-6)")
        while True:
            try:
                column = int(input())
                game_state = connect4.add_token(column)
                break
            except ValueError:  # the method raises ValueError if the input is not an int >=0 and <7
                print("invalid column, choose again")
            except connect4.FullColumnError:  # column must be unfilled (top of it must be empty), otherwise FullColumnError is raised
                print("full column, choose again")

        board = connect4.get_board()  # get board condition after the token is added
        print_board(board)
        print(game_state)
        print()

    connect4.start_new_game()  # if there is a winner or board is full, start a new game like this.
                               # when connect4 is instantiated at first, this method is called automatically.


