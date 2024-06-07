import twoSum_very_easy
import unittest

class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        self.assertEqual(twoSum_very_easy.twoSum(1, 2), 3)
        self.assertEqual(twoSum_very_easy.twoSum(0, 0), 0)
        self.assertEqual(twoSum_very_easy.twoSum(-1, 1), 0)
        self.assertEqual(twoSum_very_easy.twoSum(-1, -1), -2)
        self.assertEqual(twoSum_very_easy.twoSum(1, -1), 0)
        self.assertEqual(twoSum_very_easy.twoSum(0, 1), 1)
        self.assertEqual(twoSum_very_easy.twoSum(1, 0), 1)

if __name__ == '__main__':
    unittest.main()