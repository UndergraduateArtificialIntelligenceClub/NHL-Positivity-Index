import os 
import praw
from dotenv import load_dotenv
from datetime import datetime
from praw.models import MoreComments
import json
from extract_reddit_comments import extract_HockeyMod_comments
                
def main():
    load_dotenv()

    CLIENT_ID = os.environ["CLIENT_ID"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    username = os.environ["reddit_username"]
    password = os.environ["reddit_password"]



    reddit = praw.Reddit(
        client_id = CLIENT_ID, 
        client_secret = SECRET_KEY, 
        password = password,
        user_agent = "UAIS", 
        username = username
    )

    start_date = datetime(2023, 12, 1).date()
    end_date = datetime(2023, 12, 15).date()

    all_HockeyMod_comments = extract_HockeyMod_comments(reddit, start_date, end_date)
    json_file_path = 'december_2023_comments.json'


    with open(json_file_path, 'w') as json_file:
        json.dump(all_HockeyMod_comments, json_file)

if __name__ == "__main__":
    main()