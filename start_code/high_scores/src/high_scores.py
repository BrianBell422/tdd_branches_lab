class HighScores:

    def __init__(self, scores):
        self.scores = scores

    def latest_score(self):
        return self.scores.pop(-1)
  
    def personal_best(self):
        return max(self.scores)
    
    
    def personal_top_three(self):
        self.scores.sort()
        return self.scores[-3:]

    def highest_to_lowest(self):
        self.scores.sort()
        return self.scores.reverse()



    