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


def extract_user_comments(reddit, start_date:datetime, end_date:datetime, teams_and_users) -> list[dict]:
    """
    returns a list of dictionaries containing information about each comment on each submission of a specific user in a given time frame

    :param reddit: instance of reddit class in Praw
    :param start_date: start time of the date range
    :param end_date: end time of the date range
    :param teams_and_users: dictionary of teams and users
    :return: returns a list of dictionaries
    """

    results = []
    for subreddit_name, username in teams_and_users.items():
        subreddit = reddit.subreddit(subreddit_name)
        user = reddit.redditor(username)

        for submission in user.submissions.new():
            submission_date = datetime.utcfromtimestamp(submission.created_utc).date()
            if submission.subreddit == subreddit and start_date <= submission_date <= end_date:
                for comment in submission.comments.list():
                    if isinstance(comment, MoreComments):
                        continue
                    comment_info ={
                        'submission_id': submission.id,
                        'comment_id': comment.id,
                        'body': comment.body,
                        'score': comment.score,
                        'date': submission_date.strftime("%Y-%m-%d"),
                        'subreddit': subreddit_name
                    }
                    results.append(comment_info)
    return results


def search_flair(self,reddit: praw.reddit, subreddit: str, flairs: list) -> (list):
    """
    A method which searches through the given subbreddit under each of the given
    flairs, and returns the submissions from that flair within the last month. 

    Args:
        reddit (praw.reddit):   The reddit api connected to our reddit account
        subreddit (str):        The name of the subreddit we are searching within
        flairs (list):          A list of flairs we need to search

    Returns:
        list: all the submissions within the subreddit from all the given flairs. 
    """
    submissions = []
    
    
    for flair in flairs:
        query = flair + ": "
        for submission in reddit.subreddit(subreddit).search(query = query ,sort = "new" ,time_filter = "all" , limit = None):
            submissions.append(submission)
    
    return submissions
    
    
    
def get_all_flaired_submissions(self,reddit: praw.reddit,team_flairs: dict):
    """
    Searches through all the team's different flairs, and returns all the submission from them. 

    Args:
        reddit (praw.reddit):   The reddit api connected to our reddit account
        team_flairs (dict):     The teams and flairs we need to search through

    Returns:
        list: All submissions from the given teams and flairs. 
    """
    all_submissions = []

    # Searches through the flairs of each subreddit, and adds all the posts from the last month
    for team_subreddit in team_flairs:            
        submissions = self.search_flair(reddit = reddit, subreddit = team_subreddit, flairs= team_flairs[team_subreddit])
        all_submissions.extend(submissions)

    return all_submissions



def extract_flair_comments(self, reddit:praw.reddit,start_date: datetime, end_date: datetime):
    """
    Retrieves all the flaired comments from within the timeframe, and adds them to a list. 

    Args:
        reddit (praw.reddit): The reddit api connected to our reddit account
        start_date (datetime): The start date of collection
        end_date (datetime): The end date of collection

    Returns:
        list[dict]: A list of dictionaries of all necissary data. 
    """

    teams_and_flairs = {
        "canes" : ["GDT"],
        "NewYorkIslanders": ["GDT", "PGT"],
        "Flyers": ["Pre-Game Thread", "Post Game Thread", "Game Thread"],
        "penguins": ["GDT", "PGT"],
        "ColoradoAvalanche": ["Pre-Game Thread", "Next Day Thread", "PGT", "GDT"],
        "BostonBruins": ["Post-Game Thread", "GDT: Away"],
        "EdmontonOilers": ["GDT", "TMA", "PGT"],
        "leafs": ["Game Day Thread"]
    }
    all_flaired_comments = []
    submissions = self.get_all_submissions(reddit= reddit,team_flairs= teams_and_flairs)

    # Gets all the info from comments for each submission, and adds that data to a list. 
    for submission in submissions:
        
        subreddit_name = str(submission.subreddit)
        submission_date = datetime.utcfromtimestamp(submission.created_utc).date()
        
        
        if start_date <= submission_date <= end_date:
            for comment in submission.comments.list():
                
                if isinstance(comment, MoreComments):
                    continue
                
                comment_info = {
                    'submission_id': submission.id,
                    'comment_id': comment.id,
                    'body': comment.body,
                    'score': comment.score,
                    'date': submission_date.strftime("%Y-%m-%d"),
                    'subreddit': subreddit_name
                }
                
                all_flaired_comments.append(comment_info)
                
    return all_flaired_comments