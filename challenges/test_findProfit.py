import unittest
from findProfit_medium import profit

class TestProfit(unittest.TestCase):
    def test_profit(self):
        data = {
            "cost_price": 32.67,
            "sell_price": 45.00,
            "inventory": 1200
        }
        self.assertEqual(profit(data), 14796)

if __name__ == '__main__':
    unittest.main()