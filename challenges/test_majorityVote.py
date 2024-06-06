import unittest
from majorityVote_hard import majority_vote

class TestMajorityVote(unittest.TestCase):
    def test_majority_vote(self):
        self.assertEqual(majority_vote(["A", "A", "A", "B", "C", "A"]), "A")
        self.assertEqual(majority_vote(["A", "A", "A", "B", "B", "A"]), "A")
        self.assertEqual(majority_vote(["A", "A", "A", "A", "B", "B"]), "A")
        self.assertIsNone(majority_vote(["A", "B", "B", "A", "C", "C"]))
        self.assertEqual(majority_vote(["B", "B", "A", "B", "B", "C"]), "B")

if __name__ == '__main__':
    unittest.main()