
def has_scores(scores):
    return scores

def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def return_top_three(scores):
    top_three_scores = sorted(scores)
    return top_three_scores[-3:]

def highest_to_lowest(scores):
    rev_scores = sorted(scores)
    rev_scores.reverse()
    return rev_scores



    