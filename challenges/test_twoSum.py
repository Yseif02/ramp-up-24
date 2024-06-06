import twoSum_very_easy
import unittest

class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        self.assertEqual(twoSum_very_easy.twoSum(1, 2), 3)
        print("Test 1 passed")
        self.assertEqual(twoSum_very_easy.twoSum(0, 0), 0)
        print("Test 2 passed")
        self.assertEqual(twoSum_very_easy.twoSum(-1, 1), 0)
        print("Test 3 passed")
        self.assertEqual(twoSum_very_easy.twoSum(-1, -1), -2)
        print("Test 4 passed")
        self.assertEqual(twoSum_very_easy.twoSum(1, -1), 0)
        print("Test 5 passed")
        self.assertEqual(twoSum_very_easy.twoSum(0, 1), 1)
        print("Test 6 passed")
        self.assertEqual(twoSum_very_easy.twoSum(1, 0), 1)
        print("Test 7 passed")

if __name__ == '__main__':
    unittest.main()