from domain import *
import unittest

class Test_domain(unittest.TestCase):
    def test_valid_coord(self):
        test = Board()
        self.assertEqual(None, test.valid_coord('1', 'A'))
        self.assertRaises(ValueError, test.valid_coord, '12', 'A')
        self.assertRaises(ValueError, test.valid_coord, '1', 'Z')
        self.assertRaises(ValueError, test.valid_coord, 'abcd', 'abcd')

    def test_place_square(self):
        test = Board()
        test.place_square(0, 0, '✓')
        self.assertEqual(test.get_square(0, 0), 1)

        test.place_square(0, 0, 'X')
        self.assertEqual(test.get_square(0, 0), -1)

    def test_empty_square(self):
        test = Board()
        test.place_square(1, 0, 'X')
        self.assertRaises(ValueError, test.empty_square, '2', 'A', 'X')
        self.assertRaises(ValueError, test.empty_square, '2', 'A', '✓')

        self.assertEqual(None, test.empty_square('2', 'A', '□'))

    def test_valid_ship(self):
        test = Board()
        self.assertEqual(None, test.valid_ship(0, 0, 'S', 4))
        test.place_ship(0, 0, 'S', 4)
        self.assertRaises(ValueError, test.valid_ship, 10, 10, 'S', 4)
        self.assertRaises(ValueError, test.valid_ship, 0, 0, 'S', 4)
        self.assertRaises(ValueError, test.valid_ship, 2, 0, 'S', 4)

    def test_place_ship(self):
        test = Board()
        test.place_ship(0, 0, 'S', 3)
        self.assertEqual(2, test.get_square(0, 0))
        self.assertEqual(2, test.get_square(1, 0))
        self.assertEqual(2, test.get_square(2, 0))
        self.assertEqual(0, test.get_square(0, 1))
        self.assertEqual(0, test.get_square(3, 0))

    def test_hit_or_missed(self):
        test = Board()
        test.place_ship(0, 0, 'S', 4)
        self.assertEqual(True, test.hit_or_missed(0, 0))
        self.assertEqual(True, test.hit_or_missed(1, 0))
        self.assertEqual(False, test.hit_or_missed(4, 0))
