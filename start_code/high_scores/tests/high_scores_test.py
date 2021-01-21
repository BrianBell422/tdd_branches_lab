import unittest

from src.high_scores import HighScores

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self):
        self.score_list = HighScores([10, 15, 18, 20, 30])
    
    # Tests
    def test_has_scores(self):
        self.assertEqual([10, 15, 18, 20, 30], self.score_list.scores)

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(30, self.score_list.latest_score())

    # Test personal best (the highest score in the list)
    def test_personal_best_scores(self):
        self.assertEqual(30, self.score_list.personal_best())


    # Test top three from list of scores
    def test_personal_top_three(self):
        self.assertEqual([18, 20, 30], self.score_list.personal_top_three())

    # Test ordered from highest to lowest
    def test_highest_to_lowest(self):
        self.assertEqual([30, 20, 18, 15, 10], self.score_list.highest_to_lowest())

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one



    #
    
