# from connect4 import *
import connect4_revise as connect4
from artificial_idiot import *


def print_board(board: [[]]):
    print("============================")
    for i in range(6):
        for j in range(7):
            if board[i][j] == BoardValue.EMPTY:
                print("*", end="")
            elif board[i][j] == BoardValue.A_TOKEN:
                print("A", end="")
            elif board[i][j] == BoardValue.B_TOKEN:
                print("B", end="")
        print()
    print("============================")


if __name__ == '__main__':
    playerA = ArtificialIdiot("PlayerA")
    playerB = ArtificialIdiot("PlayerB")
    connect4 = Connect4(playerA, playerB)
    board = connect4.get_board()

    game_state = connect4.get_game_state()
    while game_state == GameState.GAME_CONTINUE:
        curr_player = connect4.get_curr_player()
        print(curr_player)
        if curr_player == playerA:
            game_state = connect4.add_token(playerA.choose_column(board))
        elif curr_player == playerB:
            game_state = connect4.add_token(playerB.choose_column(board))
        else:
            raise ValueError
        board = connect4.get_board()
        print_board(board)
        print(game_state)
        print()

    # print(connect4.get_curr_player())
    # print(connect4.add_token())
    # board = connect4.get_board()
    # print_board(board)
    # print()
    #
    # print(connect4.get_curr_player())
    # print(connect4.add_token(0))
    # board = connect4.get_board()
    # print_board(board)
    # print()
    #
    # connect4.start_new_game()
    # board = connect4.get_board()
    # print(connect4.get_curr_player())
    # print_board(board)


