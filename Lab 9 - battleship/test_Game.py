from game import*
import unittest

class Test_game(unittest.TestCase):

    def test_place_ship(self):
        test = Game()
        test.place_ship('1 A', 'S', 4)
        self.assertEqual(True, test.player_board.hit_or_missed(0, 0))
        self.assertEqual(False, test.player_board.hit_or_missed(7, 7))

        self.assertRaises(ValueError, test.place_ship, 'A1', 'S', 4)
        self.assertRaises(ValueError, test.place_ship, '10 J', 'S', 4)
        self.assertRaises(ValueError, test.place_ship, '1 A', 'SN', 4)
        self.assertRaises(ValueError, test.place_ship, '1 A', 'N', 4)
        self.assertRaises(ValueError, test.place_ship, '2 A', 'S', 3)

        test.place_ship('2 B','E', 3)
        self.assertEqual(True, test.player_board.hit_or_missed(1, 1))
        self.assertEqual(False, test.player_board.hit_or_missed(2, 1))

    def test_users_guess(self):
        test = Game()
        test.users_guess('1 A')
        self.assertNotEqual(None, test.targeting_board.hit_or_missed(0, 0))
        self.assertEqual(1, abs(test.targeting_board.get_square(0,0)))

        self.assertRaises(ValueError, test.users_guess, '1 A')

