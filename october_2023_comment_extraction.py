import os 
import praw
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ["CLIENT_ID"]
SECRET_KEY = os.environ["SECRET_KEY"]
username = os.environ["reddit_username"]
password = os.environ["reddit_password"]

print(CLIENT_ID)

reddit = praw.Reddit(
    client_id = CLIENT_ID, 
    client_secret = SECRET_KEY, 
    password = password,
    user_agent = "UAIS", 
    username = username
)

for submission in reddit.redditor("HockeyMod").submissions.new(limit = 5):
    print(submission.title)