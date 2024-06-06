import unittest
import addStrNums_medium

class TestAddStrNums(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(addStrNums_medium.add("111", "222"), "333")

    def test_add_positive_number_and_zero(self):
        self.assertEqual(addStrNums_medium.add("0", "123"), "123")

    def test_add_positive_number_and_negative_number(self):
        self.assertEqual(addStrNums_medium.add("-10", "5"), "-5")

    def test_add_two_negative_numbers(self):
        self.assertEqual(addStrNums_medium.add("-20", "-30"), "-50")

    def test_add_positive_number_and_non_numeric_string(self):
        self.assertEqual(addStrNums_medium.add("100", "abc"), "Invalid Operation")

    def test_add_two_non_numeric_strings(self):
        self.assertEqual(addStrNums_medium.add("abc", "def"), "Invalid Operation")

    def test_add_empty_string_and_number(self):
        self.assertEqual(addStrNums_medium.add("", "123"), "Invalid Operation")

    def test_add_none_and_number(self):
        self.assertEqual(addStrNums_medium.add(None, "123"), "Invalid Operation")

if __name__ == '__main__':
    unittest.main() 