import os
from dotenv import load_dotenv
import praw


class reddit_initializor:
    def __init__(self):
        load_dotenv()

        CLIENT_ID = os.environ["CLIENT_ID"]
        SECRET_KEY = os.environ["SECRET_KEY"]
        username = os.environ["reddit_username"]
        password = os.environ["reddit_password"]

        self.reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=SECRET_KEY,
            password=password,
            user_agent="UAIS",
            username=username,
        )

    def get_reddit(self) -> praw.Reddit:
        return self.reddit
