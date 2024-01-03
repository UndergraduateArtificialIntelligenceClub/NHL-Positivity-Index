import praw
import datetime
from praw.models import MoreComments

def extract_HockeyMod_comments(reddit, start_date: datetime, end_date: datetime) -> list[dict]:
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
    for submission in reddit.redditor("HockeyMod").submissions.new(limit = None):
        submission_date = datetime.utcfromtimestamp(submission.created_utc).date()
    
        if start_date <= submission_date <= end_date:
            for comment in submission.comments.list():
                if isinstance(comment, MoreComments):
                    continue
            if comment.author != "HockeyMod":
                comment_info = {
                    'submission_id': submission.id,  # id of post
                    'comment_id': comment.id,  # id of comment
                    'body': comment.body,  # comment text
                    'score': comment.score,  # number of upvotes
                    'date': submission_date.strftime('%Y-%m-%d'),  # date comment was posted on 
                    'subreddit': str(comment.subreddit)  # subreddit comment was posted in 
                }
                all_HockeyMod_comments.append(comment_info)
    return all_HockeyMod_comments