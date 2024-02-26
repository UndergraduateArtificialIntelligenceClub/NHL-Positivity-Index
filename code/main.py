import praw
from datetime import datetime
from praw.models import MoreComments
from utils import get_all_flaired_submissions
from constants import HOCKEY_MOD, TEAMS_AND_FLAIRS, TEAM_AND_USERS, TEAMS_AND_TITLES
import os
from dotenv import load_dotenv
from reddit_login import RedditInitializor
load_dotenv()
current_directory = os.environ["current_directory"]
import json
from chart_dashboard import create_positivity_score_df, create_biweekly_dashboard
from constants import SUBREDDIT_MAPPING, LABEL_SCORES
from collections import defaultdict
from reddit import CommentsExtractor
from label_data import convert_to_dataset, label_dataset

if __name__ == "__main__":
    start_date = datetime(2024, 2, 1).date()
    end_date = datetime(2024, 2, 15).date()
    reddit_initializor = RedditInitializor()
    reddit = reddit_initializor.get_reddit()
    comment_extractor = CommentsExtractor(reddit, start_date, end_date)
    feb1_feb15_comments = comment_extractor.extract_comments()
    with open(f'{current_directory}/data/February_data/feb1_to_feb15_data.json', 'w') as fp:
        json.dump(feb1_feb15_comments, fp)

    
    content_dataset = convert_to_dataset(
        f'{current_directory}/data/February_data/clean_feb1_to_feb15_data.json'
    )
    labelled_dataset = label_dataset(content_dataset)
    labelled_dataset.to_json(f'{current_directory}/data/February_data/labelled_feb1_to_feb15_data.json')
    with open(f'{current_directory}/data/February_data/labelled_feb1_to_feb15_data.json', 'r') as fp:
        
        
        positivity_scores = defaultdict(int)
        count_scores = defaultdict(int)
        for data in fp:
            data = json.loads(data)
            team = SUBREDDIT_MAPPING.get(data["subreddit"],None)
            if team is None:
                print("Team not found: ")
                print(data["subreddit"])
                continue
            positivity_scores[team] += (data["score"] + 1)*LABEL_SCORES[data["label"]["label"]] # add 1 to score to make sure to not multiply by 0
            count_scores[team] += 1
    
    team_scores = {}
    for key in positivity_scores.keys():
        if count_scores[key]!=0:
            score = positivity_scores[key]/count_scores[key]
        team_scores[key] = score
    with open(f'{current_directory}/data/February_data/team_pos_scores_feb1_to_feb15_datav2.json', 'w') as fp:
        json.dump(team_scores, fp)
        
    df = create_positivity_score_df(team_scores)
    create_biweekly_dashboard(df)