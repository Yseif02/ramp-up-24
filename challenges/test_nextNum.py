import nextNum_very_easy
import unittest

class TestNextNum(unittest.TestCase):
    def test_nextNum(self):
        self.assertEqual(nextNum_very_easy.nextNum(0), 1)
        print("Test 1 passed")
        self.assertEqual(nextNum_very_easy.nextNum(1), 2)
        print("Test 2 passed")
        self.assertEqual(nextNum_very_easy.nextNum(-1), 0)
        print("Test 3 passed")
        self.assertEqual(nextNum_very_easy.nextNum(10), 11)
        print("Test 4 passed")
        self.assertEqual(nextNum_very_easy.nextNum(-10), -9)
        print("Test 5 passed")

if __name__ == '__main__':
    unittest.main()