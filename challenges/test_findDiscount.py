import unittest
from findDiscount_easy import calculate_final_price

class TestCalculateFinalPrice(unittest.TestCase):
    def test_calculate_final_price(self):
        self.assertEqual(calculate_final_price(1500, 50), 750)
        self.assertEqual(calculate_final_price(89, 20), 71.2)
        self.assertEqual(calculate_final_price(100, 75), 25)

if __name__ == '__main__':
    unittest.main()