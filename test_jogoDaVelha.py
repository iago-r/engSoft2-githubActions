# test_tic_tac_toe.py

import unittest
from jogoDaVelha import TicTacToe  # importando a classe do outro arquivo

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_check_win_row(self):
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(self.game.check_win(), 'X')

    def test_check_win_column(self):
        self.game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertEqual(self.game.check_win(), 'X')

    def test_check_win_diagonal(self):
        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertEqual(self.game.check_win(), 'X')

    def test_check_win_no_win(self):
        self.game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        self.assertEqual(self.game.check_win(), 'Draw')  # Espera 'Draw' em vez de False

    def test_check_win_draw(self):
        self.game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertEqual(self.game.check_win(), 'Draw')

if __name__ == '__main__':
    unittest.main()
