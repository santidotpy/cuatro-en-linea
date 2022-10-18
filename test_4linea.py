import unittest
from unittest.mock import patch
from parameterized import parameterized
from four_main import Board

class Test_4Linea(unittest.TestCase):

    def setUp(self):
         self.b = Board()

    # si esta fuera de mis limites es IndexError
    @parameterized.expand([ (9,), (10,), (80,), (55,), (8,), (215,), (22,), (18,)])
    def test_out_of_range(self, param):
        with self.assertRaises(IndexError):
            self.b.turn(param)

    @parameterized.expand([ ('a',), ('b',), ('$',), ('P',), ('#',), ('o',), ('5',), ('@',)])
    def test_enter_not_int(self, param):
        with self.assertRaises(ValueError):
            self.b.turn(param)

    @parameterized.expand([ (1,), (4,), (5,), (3,), (1,), (1,), (6,), (2,), (3,)])
    def test_in_range(self, param):
        move = self.b.turn(param)
        self.assertTrue(move)

    def test_check_turn(self):
        n = Board()
        params = [(1, '🍎'), (1, '🍏'), (5, '🍎'), (3, '🍏')]
        for t, p in params:
            n.turn(t)
            fun = n.which_turn()
            with self.subTest():
                self.assertEqual(fun, p)

    @parameterized.expand([ (1, 3,), (5, 2), (3, 2), (4, 4), (1, 2)])
    def test_check_limits_ok(self, row, col):
        move = self.b.check_limits(row, col)
        self.assertTrue(move)

    @parameterized.expand([ (9, 9), (-1, -1), (-5, 10), (15, -4), (1, 20), (18, 2)])
    def test_check_limits_wrong(self, row, col):
        move = self.b.check_limits(row, col)
        self.assertFalse(move)

    def test_check_winner_green(self):
        playing = Board()
        playing.turn(1)
        playing.turn(2)
        playing.turn(1)
        playing.turn(2)
        playing.turn(1)
        playing.turn(2)
        playing.turn(1)
        c, player = playing.check_winner()
        self.assertTrue(c)
        self.assertEqual(player, '🍏')

    def test_check_winner_red(self):
        playing = Board()
        playing.turn(5)
        playing.turn(2)
        playing.turn(3)
        playing.turn(2)
        playing.turn(1)
        playing.turn(2)
        playing.turn(4)
        playing.turn(2)
        c, player = playing.check_winner()
        self.assertTrue(c)
        self.assertEqual(player, '🍎')

    @parameterized.expand([ (1,), (4,), (2,),(4,), (3,),(4,),(1,),(4,)])
    def test_check_no_winner(self, param):
        playing = Board()
        playing.turn(param)
        c, player = playing.check_winner()
        self.assertIsNone(player)
        self.assertFalse(c)

        


if __name__ == '__main__':
    unittest.main()