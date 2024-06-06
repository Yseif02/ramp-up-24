import unittest
from combinedConsecutiveArray_hard import consecutive_combo

class TestConsecutiveCombo(unittest.TestCase):
    def test_consecutive_combo(self):
        self.assertTrue(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
        self.assertFalse(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
        self.assertFalse(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
        self.assertTrue(consecutive_combo([44, 46], [45]))
        self.assertTrue(consecutive_combo([4, 3, 1], [2, 5]))
        self.assertTrue(consecutive_combo([4, 3, 1], [2, 5, 6]))

if __name__ == '__main__':
    unittest.main()