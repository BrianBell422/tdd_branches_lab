import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    
    def setUp(self):
        self.home_win = {"home_score": 3, "away_score": 2}
        self.away_win =  {"home_score": 0, "away_score": 2}
        self.draw = {"home_score": 1, "away_score": 1}
        self.final_scores = [self.home_win, self.away_win, self.draw]


    
    
    
    
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
