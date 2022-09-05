import unittest
from collection import*
import random

class TestModule(unittest.TestCase):
    def test_collection(self):
        test = Collection()
        self.assertEqual(0, len(test))
        test.append(0)
        test.append(1)
        self.assertEqual(2, len(test))

    def test_remove_collection(self):
        test = Collection()
        for i in range(0, 10):
            test.append(i)
        test.remove(5)
        self.assertEqual(test[5], 6)
        self.assertEqual(len(test), 9)

    def comp_func(self, a, b):
        if a == b:
            return 0
        if a < b:
            return -1
        return 1

    def test_sort(self):
        test = Collection()
        l = list(range(0,10))
        random.shuffle(l)
        for elem in l:
            test.append(elem)
        sort(test, self.comp_func, 1)
        self.assertEqual(test[1], 1)
        self.assertEqual(test[5], 5)

    def filter_func(self, a):
        if a % 2 == 0:
            return 1
        return 0

    def test_filter(self):
        test = Collection()
        for elem in range(0, 10):
            test.append(elem)
        test = filter(test, self.filter_func)
        self.assertEqual(len(test), 5)
        self.assertEqual(test[2], 4)

if __name__ == '__main__':
    unittest.main()