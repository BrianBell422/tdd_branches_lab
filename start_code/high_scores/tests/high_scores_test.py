import unittest

from src.high_scores import latest, has_scores, personal_best, return_top_three, highest_to_lowest

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def test_has_scores(self):
        scores = [100, 0, 90, 30]
        expected = [100, 0, 90, 30]
        self.assertEqual(expected, has_scores(scores)) 

    def test_latest(self):
        scores = [100, 0, 90, 30]
        expected = 30
        self.assertEqual(expected, latest(scores))

    def test_personal_best(self):
        scores = [100, 0, 90, 30, 45, 10]
        expected = 100
        self.assertEqual(expected, personal_best(scores))

    def test_return_top_three(self):
        scores = [100, 0, 90, 30, 45, 10]
        expected = [45, 90, 100]
        self.assertEqual(expected, return_top_three(scores))

    def test_highest_to_lowest(self):
        scores = [100, 0, 90, 30, 45, 10]
        expected = [100, 90, 45, 30, 10, 0]
        self.assertEqual(expected, highest_to_lowest(scores))

    def test_top_three_tie(self):
        scores = [100, 100, 100, 30, 45, 10]
        expected = [100, 100, 100]
        self.assertEqual(expected, return_top_three(scores))

    def test_top_three_less_than_three(self):
        scores = [100, 90]
        expected = [90, 100]
        self.assertEqual(expected, return_top_three(scores))

    def test_top_three_one(self):
        scores = [100]
        expected = [100]
        self.assertEqual(expected, return_top_three(scores))

if __name__ == "__main__":
    unittest.main()
