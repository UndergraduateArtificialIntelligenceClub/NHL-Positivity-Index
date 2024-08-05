import praw
from datetime import datetime
from praw.models import MoreComments
from utils import get_all_flaired_submissions, clean_title, title_contains_draft_key_words
from constants import HOCKEY_MOD, TEAMS_AND_FLAIRS, TEAM_AND_USERS, TEAMS_AND_TITLES, SUBREDDIT_MAPPING
import os
from dotenv import load_dotenv
from reddit_login import RedditInitializor
load_dotenv()
current_directory = os.environ["current_directory"]
import json

class CommentsExtractor:
    def __init__(self, reddit, start_date: datetime, end_date: datetime):
        self.reddit = reddit
        self.start_date = start_date
        self.end_date = end_date

    def extract_HockeyMod_comments(self) -> list[dict]:
        """Returns a list of dictionaries which contain information from every comment on a
        post posted by u/HockeyMod on Reddit in recent given time frame

        Args:
            reddit (Reddit): An instance of the Reddit class in PRAW
            start_date (datetime): start time of the date range
            end_date (datetime): end time of the date range

        Returns:
            list[dict]: A dictionary containing information about a comment
        """
        all_HockeyMod_comments = []
        for submission in self.reddit.redditor(HOCKEY_MOD).submissions.new(limit=None):
            submission_date = datetime.utcfromtimestamp(submission.created_utc).date()

            if self.start_date <= submission_date <= self.end_date:
                for comment in submission.comments.list():
                    if isinstance(comment, MoreComments):
                        continue
                    if comment.author != HOCKEY_MOD:
                        comment_info = {
                            "submission_id": submission.id,  # id of post
                            "comment_id": comment.id,  # id of comment
                            "body": comment.body,  # comment text
                            "score": comment.score,  # number of upvotes
                            "date": submission_date.strftime(
                                "%Y-%m-%d"
                            ),  # date comment was posted on
                            "subreddit": str(
                                comment.subreddit
                            ),  # subreddit comment was posted in
                        }
                        all_HockeyMod_comments.append(comment_info)
        return all_HockeyMod_comments

    def extract_user_comments(self) -> list[dict]:
        """
        returns a list of dictionaries containing information about each comment on each submission of a specific user in a given time frame

        :param reddit: instance of reddit class in Praw
        :param start_date: start time of the date range
        :param end_date: end time of the date range
        :param teams_and_users: dictionary of teams and users
        :return: returns a list of dictionaries
        """

        results = []
        for subreddit_name, username in TEAM_AND_USERS.items():
            subreddit = self.reddit.subreddit(subreddit_name)
            user = self.reddit.redditor(username)

            for submission in user.submissions.new():
                submission_date = datetime.utcfromtimestamp(
                    submission.created_utc
                ).date()
                if (
                    submission.subreddit == subreddit
                    and self.start_date <= submission_date <= self.end_date
                ):
                    for comment in submission.comments.list():
                        if isinstance(comment, MoreComments):
                            continue
                        comment_info = {
                            "submission_id": submission.id,
                            "comment_id": comment.id,
                            "body": comment.body,
                            "score": comment.score,
                            "date": submission_date.strftime("%Y-%m-%d"),
                            "subreddit": subreddit_name,
                        }
                        results.append(comment_info)
        return results
    
    def extract_user_comments(self) -> list[dict]:
        """
        returns a list of dictionaries containing information about each comment on each submission of a specific user in a given time frame

        :param reddit: instance of reddit class in Praw
        :param start_date: start time of the date range
        :param end_date: end time of the date range
        :param teams_and_users: dictionary of teams and users
        :return: returns a list of dictionaries
        """

        results = []
        for subreddit_name, username in TEAM_AND_USERS.items():
            subreddit = self.reddit.subreddit(subreddit_name)
            user = self.reddit.redditor(username)

            for submission in user.submissions.new():
                submission_date = datetime.utcfromtimestamp(
                    submission.created_utc
                ).date()
                if (
                    submission.subreddit == subreddit
                    and self.start_date <= submission_date <= self.end_date
                ):
                    for comment in submission.comments.list():
                        if isinstance(comment, MoreComments):
                            continue
                        comment_info = {
                            "submission_id": submission.id,
                            "comment_id": comment.id,
                            "body": comment.body,
                            "score": comment.score,
                            "date": submission_date.strftime("%Y-%m-%d"),
                            "subreddit": subreddit_name,
                        }
                        results.append(comment_info)
        return results
    
    def extract__start_title_comments(self) -> list[dict:]:
        """
        returns a list of dictionaries containing information about each comment on each submission of a specific title in a given time frame

        :param reddit: instance of reddit class in Praw
        :param start_date: start time of the date range
        :param end_date: end time of the date range
        :param teams_and_titles: dictionary of teams and titles
        :return: returns a list of dictionaries
        """
        results = []
        for subreddit_name in TEAMS_AND_TITLES.keys():
            subreddit = self.reddit.subreddit(subreddit_name)
            
            for start_word in TEAMS_AND_TITLES[subreddit_name]: 
                search_query = f'title:"{start_word}*"'

                for submission in subreddit.search(search_query, sort='new'):
                    submission_date = datetime.utcfromtimestamp(submission.created_utc).date()
                    if self.start_date <= submission_date <= self.end_date:
                        for comment in submission.comments.list():
                            if isinstance(comment, MoreComments):
                                continue
                            comment_info = {
                                "submission_id": submission.id,
                                "comment_id": comment.id,
                                "body": comment.body,
                                "score": comment.score,
                                "date": submission_date.strftime("%Y-%m-%d"),
                                "subreddit": subreddit_name,
                            }
                            results.append(comment_info)
        return results

    def extract_flair_comments(self):
        """
        Retrieves all the flaired comments from within the timeframe, and adds them to a list.

        Args:
            reddit (praw.reddit): The reddit api connected to our reddit account
            start_date (datetime): The start date of collection
            end_date (datetime): The end date of collection

        Returns:
            list[dict]: A list of dictionaries of all necissary data.
        """
        all_flaired_comments = []
        submissions = get_all_flaired_submissions(
            reddit=self.reddit, team_flairs=TEAMS_AND_FLAIRS
        )

        # Gets all the info from comments for each submission, and adds that data to a list.
        for submission in submissions:

            subreddit_name = str(submission.subreddit)
            submission_date = datetime.utcfromtimestamp(submission.created_utc).date()

            if self.start_date <= submission_date <= self.end_date:
                for comment in submission.comments.list():

                    if isinstance(comment, MoreComments):
                        continue

                    comment_info = {
                        "submission_id": submission.id,
                        "comment_id": comment.id,
                        "body": comment.body,
                        "score": comment.score,
                        "date": submission_date.strftime("%Y-%m-%d"),
                        "subreddit": subreddit_name,
                    }

                    all_flaired_comments.append(comment_info)

        return all_flaired_comments
    
    def extract_draft_comments_from_submissions(self) -> list[dict:]:
        """
        returns a list of dictionaries containing information about each comment on each submission of a title containing draft relevant
        information in a given time frame

        :param reddit: instance of reddit class in Praw
        :param start_date: start time of the date range
        :param end_date: end time of the date range
        :param teams_and_titles: dictionary of teams and titles
        :return: returns a list of dictionaries
        """
        results = []
        for subreddit_name in SUBREDDIT_MAPPING.keys():
            
            subreddit = self.reddit.subreddit(subreddit_name)
            for submission in subreddit.new(limit=None):
                submission_date = datetime.utcfromtimestamp(submission.created_utc).date()
            
                if self.start_date <= submission_date <= self.end_date:    
                    if title_contains_draft_key_words(submission.title):
                        for comment in submission.comments.list():
                            if isinstance(comment, MoreComments):
                                continue
                            comment_info = {
                                "submission_id": submission.id,
                                "comment_id": comment.id,
                                "body": comment.body,
                                "score": comment.score,
                                "date": submission_date,
                                "subreddit": subreddit_name,
                            }
                            results.append(comment_info)        
        return results
    

    def extract_comments(self):
        result = []
        result.extend(self.extract_HockeyMod_comments())
        result.extend(self.extract_user_comments())
        result.extend(self.extract_flair_comments())
        result.extend(self.extract_start_title_comments())
        return result
    
    def extract_draft_comments(self):
        result = []
        result.extend(self.extract_draft_comments_from_submissions())
        return result
    
    

