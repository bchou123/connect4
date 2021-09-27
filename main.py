""" This file is a example of how this API works.

"""

from connect4 import *
from randombot import RandomBot


def print_board(board: [[]]):
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
    playerA = RandomBot("PlayerA")  # playerA is an instance of a subclass of Player. Refer to randombot.py
    playerB = Player("PlayerB")  # playerB is an instance of Player.
    connect4 = Connect4(playerA, playerB)  # instantiate Connect4
    board = connect4.get_board()  # get board from connect4
    print_board(board)  # an empty board is shown

    game_state = connect4.get_game_state()  # get the current game state (should be GAME_CONTINUE at beginning
    while game_state == GameState.GAME_CONTINUE:  # while there is no winner, and the board is not full, the game can continue
        curr_player = connect4.get_curr_player()  # get current player for this round
        print(curr_player)
        if curr_player == playerA:
            playerA_column = playerA.choose_column(board)  # playerA choose a column. Refer to randombot.py
            game_state = connect4.add_token(playerA_column)  # use add_token method to add a token for current player to the chosen column
                                                             # renew game_state like this to see if there is a winner
        elif curr_player == playerB:
            playerB_column = playerB.choose_column(board)  # playerB choose a column by the default method (input from console)
            while playerB_column < 0 or playerB_column >= 7:  # column must >=0 and <=6
                print("invalid column, choose again")
                playerB_column = playerB.choose_column(board)
            game_state = connect4.add_token(playerB_column)
        board = connect4.get_board()  # get board condition after the token is added
        print_board(board)
        print(game_state)
        print()

    connect4.start_new_game()  # if there is a winner or board is full, start a new game like this.
                               # when connect4 is instantiated at first, this method is called automatically.
