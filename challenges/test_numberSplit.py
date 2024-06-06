import unittest
from numberSplit_easy import number_split

class TestNumberSplit(unittest.TestCase):
    def test_number_split_even(self):
        self.assertEqual(number_split(4), [2, 2])
        self.assertEqual(number_split(10), [5, 5])
        self.assertEqual(number_split(100), [50, 50])

    def test_number_split_odd(self):
        self.assertEqual(number_split(5), [2, 3])
        self.assertEqual(number_split(11), [5, 6])
        self.assertEqual(number_split(99), [49, 50])

if __name__ == '__main__':
    unittest.main()