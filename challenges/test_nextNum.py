import nextNum_very_easy
import unittest

class TestNextNum(unittest.TestCase):
    def test_nextNum(self):
        self.assertEqual(nextNum_very_easy.nextNum(0), 1)
        self.assertEqual(nextNum_very_easy.nextNum(1), 2)
        self.assertEqual(nextNum_very_easy.nextNum(-1), 0)
        self.assertEqual(nextNum_very_easy.nextNum(10), 11)
        self.assertEqual(nextNum_very_easy.nextNum(-10), -9)

if __name__ == '__main__':
    unittest.main()