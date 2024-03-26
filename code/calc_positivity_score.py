from constants import SUBREDDIT_MAPPING, LABEL_SCORES
from collections import defaultdict

def calc_positivity_score(dataset):
    positivity_scores = defaultdict(int)
    count_scores = defaultdict(int)
    for data in dataset:
        team = SUBREDDIT_MAPPING.get(data["subreddit"],None)
        if team is None:
            print("Team not found: ")
            print(data["subreddit"])
            continue
        positivity_scores[team] += ((1 if data["score"] < 0 else data["score"]) + 1) * LABEL_SCORES[data["label"]["label"]] # add 1 to score to make sure to not multiply by 0
        count_scores[team] += 1
    return positivity_scores,count_scores


    