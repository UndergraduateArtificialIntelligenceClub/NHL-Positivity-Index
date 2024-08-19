import logging

logging.basicConfig(level=logging.ERROR)
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
from comment_preprocessing import process_comments
import warnings
import tensorflow as tf

if __name__ == "__main__":
    tf.get_logger().setLevel('ERROR')

    warnings.filterwarnings('ignore', category=UserWarning, module='tensorflow')

    logging.getLogger("transformers").setLevel(logging.ERROR)
#     start_date = datetime(2024, 7, 1).date()
#     end_date = datetime(2024, 8, 18).date()
#     reddit_initializor = RedditInitializor()
#     reddit = reddit_initializor.get_reddit()
#     comment_extractor = CommentsExtractor(reddit, start_date, end_date)
    
#     #Free Agent Comments
#     # oilers_freeagent_key_words = ["Jeff Skinner", "Viktor", "Viktor Arvidsson", "Arvidsson", "free agent", "free agency", "3 million"]
#     # free_agent_comments = comment_extractor.extract_specific_event_comments(subreddit_name = "EdmontonOilers", keywords = oilers_freeagent_key_words)
    
#     # Offer Sheet Comments
#     # oilers_offersheet_key_words = ["offer sheet", "Broberg", "Holloway"]
#     # offersheet_comments = comment_extractor.extract_specific_event_comments(subreddit_name = "EdmontonOilers", keywords = oilers_offersheet_key_words)
    
#     # GM Comments
#     # oilers_gm_key_words = ["Bowman"]
#     # gm_comments = comment_extractor.extract_specific_event_comments(subreddit_name = "EdmontonOilers", keywords = oilers_gm_key_words)
    
#     # Stamkos Comments 
#     stamkos_key_words = ["Stamkos", "Stammer", "Steven Stamkos"]
#     stamkos_comments = comment_extractor.extract_specific_event_comments(subreddit_name = "Predators", keywords = stamkos_key_words)

# with open(f'{current_directory}/data/offseason_data/stamkos_data_24.json', 'w', encoding='utf-8') as fp:
#     json.dump(stamkos_comments, fp, ensure_ascii= False, indent = 4, default = str)
    
# cleaned_stamkos_comments = process_comments(f'{current_directory}/data/offseason_data/stamkos_data_24.json')
# with open(f'{current_directory}/data/offseason_data/clean_stamkos_data_24.json', 'w', encoding='utf-8') as fp:
#     json.dump(cleaned_stamkos_comments, fp, ensure_ascii= False, indent = 4, default = str)
        
   
    with open(f'{current_directory}/data/offseason_data/labelled_stamkos_data_24.json', 'r') as fp:
        
        
        positivity_scores = defaultdict(int)
        count_scores = defaultdict(int)
        for data in fp:
            data = json.loads(data)
            team = SUBREDDIT_MAPPING.get(data["subreddit"],None)
            if team is None:
                print("Team not found: ")
                print(data["subreddit"])
                continue
            positivity_scores[team] += ((1 if data["score"] < 0 else data["score"]) + 1) * LABEL_SCORES[data["label"]["label"]] # add 1 to score to make sure to not multiply by 0
            count_scores[team] += 1
    
    team_scores = {}
    for key in positivity_scores.keys():
        if count_scores[key]!=0:
            score = positivity_scores[key]/count_scores[key]
        team_scores[key] = score
    with open(f'{current_directory}/data/positivity_scores/offseason/pos_scores_stamkos_24.json', 'w') as fp:
        json.dump(team_scores, fp)
        
