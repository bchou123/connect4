import collections
import random
from enum import Enum
from typing import List


class GameState(Enum):
  """Represents the current state of the connect4 game
  - GAME_CONTINUE : no players have won yet, game is still ongoing.
  - PLAYER_WON : the player who made the most recent move has won.
  - BOARD_FULL : the board is full, no additional tokens can be added, no players have won.
  """
  BOARD_FULL = 0
  PLAYER_WIN = 1
  GAME_CONTINUE = 2


class BoardValue(Enum):
  """Represents the possible values in the connect4 game board"""
  EMPTY = 0
  A_TOKEN = 1
  B_TOKEN = 2


class Player(object):
  """This class represents a player.
  """

  # name = ""

  def __init__(self, n : str):
    """Constructor for the player class.
    """
    self.name = n

  def __str__(self):
    return self.name

  def choose_column(self, board:[[]]):
    pass


class Connect4(object):
  """This class represents a Connect4 game. The game board is represented by a
  2D BoardValue array with 6 rows and 7 columns. The index of the rows
  increases from top to bottom and the index of the columns increases from left
  to right for the corresponding game board.
  """

  def __init__(self, player_a: Player, player_b: Player):
    """Constructor for the Connect4 game.

    Parameters
    ----
    player_a : `Player` - one player of the game.

    player_b : `Player` - the other player of the game.

    Return Value
    ----
    result : `Connect4` - an object representing a Connect4 game.

    Exceptions
    ----
    TypeError - thrown when either playerA or playerB is not of type `Player` or
    is None.

    SamePlayerException - thrown when playerA and playerB is the same player.

    Sample Code
    ----
    """

    if player_a != player_b:
      self._players = [player_a, player_b]
      self.start_new_game()
    else:
      raise Connect4.SamePlayerException

  def get_game_state(self) -> GameState:
    """Returns the current game state.

    Parameters
    ----
    None.

    Return Value
    ----
    result : `GameState` - current state of the game

    Exceptions
    ----
    None.

    Sample Code
    ----
    """
    return self._game_state

  def get_curr_player(self) -> Player:
    """Returns the current player for this turn.

    Parameters
    ----
    None.

    Return Value
    ----
    player : `Player` - the player playing this turn.

    Exceptions
    ----
    None.

    Sample Code
    ----
    """

    return self._players[self._curr_player_index]

  def get_board(self) -> List[List[BoardValue]]:
    """Returns the current board state.

    Parameters
    ----
    None.

    Return Value
    ----
    board : `List[List[BoardValue]]` - returns a copy of the current board state
    as a 2D array.

    Exception
    ----
    None.

    Sample Code
    ----
    """

    ret = [[] for a in range(6)]
    for i in range(6):
      for j in range(7):
        if self._board[i][j] == -1:
          ret[i].append(BoardValue.EMPTY)
        elif self._board[i][j] == 0:
          ret[i].append(BoardValue.A_TOKEN)
        elif self._board[i][j] == 1:
          ret[i].append(BoardValue.B_TOKEN)

    return ret

  def add_token(self, column: int) -> GameState:
    """Adds a token to the column for the current player. Token is always placed
    at the bottom-most empty row of that column.

    Parameters
    ----
    column : `int` - the column on the board to place the check. 0 <= column < 7

    Return Value
    ----
    result : `GameState` - indicates the state of the game after adding the token.

    Exceptions
    ----
    ValueError - thrown when column is out of bounds

    FullColumnException - thrown when trying to add a token to a full column.

    GameOverException - thrown when there is already a winner or board is full.

    Sample Code
    ----
    """
    # # print("board before")
    # self._# print_board()
    if self._game_state != GameState.GAME_CONTINUE:
      raise Connect4.GameOverException
    if column < 0 or column >= 7:
      raise ValueError
    if self._board[0][column] != -1:
      raise Connect4.FullColumnException

    row = 0
    for row in range(1, 7):
      if row == 6:
        self._board[5][column] = self._curr_player_index
        break
      if self._board[row][column] != -1:
        self._board[row - 1][column] = self._curr_player_index
        break

    # # print("board after")
    # self._# print_board()

    self._game_state = self._calc_game_state(row - 1, column)
    self._board[row - 1][column] = self._curr_player_index
    self._curr_player_index ^= 1
    return self._game_state

  def start_new_game(self) -> None:
    """Starts a new connect4 game by emptying the game board. The first player
    is selected randomly.

    Parameters
    ----
    None.

    Return Value
    ----
    None.

    Exceptions
    ----
    None.

    Sample Code
    ----

    """

    for i in range(0, 6):
      for j in range(0, 7):
        self._board[i][j] = -1
    self._curr_player_index = self._random_select_start_player()
    self._game_state = GameState.GAME_CONTINUE
    self._player_lines = {}

  def _random_select_start_player(self) -> int:
    return random.randint(0, 1)

  def _calc_game_state(self, new_row: int, new_column: int) -> GameState:
    if new_row == 0:
      is_full = True
      for c in self._board[0]:
        if c == -1:
          is_full = False
          break
      if is_full:
        # print("_calc_game_state: full")
        return GameState.BOARD_FULL

    # ========================= new token at first of connect4
    if new_row >= 3:  # 0
      if self._board[new_row - 1][new_column] == self._curr_player_index \
          and self._board[new_row - 2][new_column] == self._curr_player_index \
          and self._board[new_row - 3][new_column] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "0")
        return GameState.PLAYER_WIN

    if new_row >= 3 and new_column <= 3:  # 45
      if self._board[new_row - 1][new_column + 1] == self._curr_player_index \
          and self._board[new_row - 2][new_column + 2] == self._curr_player_index \
          and self._board[new_row - 3][new_column + 3] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "1")
        return GameState.PLAYER_WIN

    if new_column <= 3:  # 90
      if self._board[new_row][new_column + 1] == self._curr_player_index \
          and self._board[new_row][new_column + 2] == self._curr_player_index \
          and self._board[new_row][new_column + 3] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "2")
        return GameState.PLAYER_WIN

    if new_row <= 2 and new_column <= 3:  # 135
      if self._board[new_row + 1][new_column + 1] == self._curr_player_index \
          and self._board[new_row + 2][new_column + 2] == self._curr_player_index \
          and self._board[new_row + 3][new_column + 3] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "3")
        return GameState.PLAYER_WIN

    if new_row <= 2:  # 180
      if self._board[new_row + 1][new_column] == self._curr_player_index \
          and self._board[new_row + 2][new_column] == self._curr_player_index \
          and self._board[new_row + 3][new_column] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "4")
        return GameState.PLAYER_WIN

    if new_row <= 2 and new_column >= 3:  # 225
      if self._board[new_row + 1][new_column - 1] == self._curr_player_index \
          and self._board[new_row + 2][new_column - 2] == self._curr_player_index \
          and self._board[new_row + 3][new_column - 3] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "5")
        return GameState.PLAYER_WIN

    if new_column >= 3:  # 270
      if self._board[new_row][new_column - 1] == self._curr_player_index \
          and self._board[new_row][new_column - 2] == self._curr_player_index \
          and self._board[new_row][new_column - 3] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "6")
        return GameState.PLAYER_WIN

    if new_row >= 3 and new_column >= 3:  # 315
      if self._board[new_row - 1][new_column - 1] == self._curr_player_index \
          and self._board[new_row - 2][new_column - 2] == self._curr_player_index \
          and self._board[new_row - 3][new_column - 3] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "7")
        return GameState.PLAYER_WIN

    # ========================= new token at second of connect4
    if 2 <= new_row <= 4:  # 0
      if self._board[new_row + 1][new_column] == self._curr_player_index \
          and self._board[new_row - 1][new_column] == self._curr_player_index \
          and self._board[new_row - 2][new_column] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "10")
        return GameState.PLAYER_WIN

    if 2 <= new_row <= 4 and 1 <= new_column <= 4:  # 45
      if self._board[new_row + 1][new_column - 1] == self._curr_player_index \
          and self._board[new_row - 1][new_column + 1] == self._curr_player_index \
          and self._board[new_row - 2][new_column + 2] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "11")
        return GameState.PLAYER_WIN

    if 1 <= new_column <= 4:  # 90
      if self._board[new_row][new_column - 1] == self._curr_player_index \
          and self._board[new_row][new_column + 1] == self._curr_player_index \
          and self._board[new_row][new_column + 2] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "12")
        return GameState.PLAYER_WIN

    if 1 <= new_row <= 3 and 1 <= new_column <= 4:  # 135
      if self._board[new_row - 1][new_column - 1] == self._curr_player_index \
          and self._board[new_row + 1][new_column + 1] == self._curr_player_index \
          and self._board[new_row + 2][new_column + 2] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "13")
        return GameState.PLAYER_WIN

    if 1 <= new_row <= 3:  # 180
      if self._board[new_row - 1][new_column] == self._curr_player_index \
          and self._board[new_row + 1][new_column] == self._curr_player_index \
          and self._board[new_row + 2][new_column] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "14")
        return GameState.PLAYER_WIN

    if 1 <= new_row <= 3 and 2 <= new_column <= 5:  # 225
      if self._board[new_row - 1][new_column + 1] == self._curr_player_index \
          and self._board[new_row + 1][new_column - 1] == self._curr_player_index \
          and self._board[new_row + 2][new_column - 2] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "15")
        return GameState.PLAYER_WIN

    if 2 <= new_column <= 5:  # 270
      if self._board[new_row][new_column + 1] == self._curr_player_index \
          and self._board[new_row][new_column - 1] == self._curr_player_index \
          and self._board[new_row][new_column - 2] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "16")
        return GameState.PLAYER_WIN

    if 2 <= new_row <= 4 and 2 <= new_column <= 5:  # 315
      if self._board[new_row + 1][new_column + 1] == self._curr_player_index \
          and self._board[new_row - 1][new_column - 1] == self._curr_player_index \
          and self._board[new_row - 2][new_column - 2] == self._curr_player_index:
        # print("_calc_game_state", self._curr_player_index, "17")
        return GameState.PLAYER_WIN

    return GameState.GAME_CONTINUE

  def _print_board(self):
    print("====================")
    for i in range(6):
      for j in range(7):
        print(self._board[i][j], end="\t")
      print()
    print("====================")

  class _Line(object):
    start_row = -1
    start_column = -1
    end_row = -1
    end_column = -1

    def __init__(self, sr, sc, er, ec):
      self.start_row = sr
      self.start_column = sc
      self.end_row = er
      self.end_column = ec

  class SamePlayerException(Exception):
    """Thrown when the 2 players of a Connect4 game are the same"""
    pass

  class FullColumnException(Exception):
    """Thrown when attempting to add token to a full column."""
    pass

  class GameOverException(Exception):
    """Thrown when attempting to add token to the board when the game is already
    over (either a player won or the board is full).
    """
    pass
