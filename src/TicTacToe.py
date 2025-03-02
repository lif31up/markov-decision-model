import numpy as np

class TicTacToe:
  def __init__(self):
    self.board = np.zeros((3, 3), dtype=int)
    self.game_over, self.winner = False, None
    self.players, self.curr_player = [1, 2], 1
    self.n_row, self.n_col = 3, 3
  # __init__
  def reset(self): self.board, self.game_over, self.winner = np.zeros((3, 3), dtype=int), False, None

  def is_valid_move(self, row, col): return self.board[row, col] == 0

  def make_move(self, row, col):
    if self.is_valid_move(row, col):
      self.board[row, col] = self.curr_player
      if self.check_win():
        self.game_over = True
        self.winner = self.curr_player
      # if
      elif np.all(self.board != 0): self.game_over = True
      else: self.curr_player = 3 - self.curr_player
    return False
  # make_move
  def check_win(self):
    for player in [1, 2]:
      if np.any(np.all(self.board == player, axis=1),) or\
        np.any(np.all(self.board == player, axis=0), ) or\
        np.all(np.diag(self.board) == player) or\
        np.all(np.diag(np.fliplr(self.board)) == player):
        return True
    # for if
    return False
  # check_win
  def get_state(self): return self.board.flatten()
  def get_valid_moves(self): return [(row, col) for row in range(3) for col in range(3) if self.board[row, col] == 0]
# TicTacToe

if __name__ == "__main__":
  three_t = TicTacToe()
  three_t.make_move(1, 2)
  three_t.make_move(0, 0)
  three_t.make_move(1, 1)
  three_t.make_move(2, 0)
  three_t.make_move(1, 0)
  print(three_t.board, three_t.game_over, three_t.winner)
