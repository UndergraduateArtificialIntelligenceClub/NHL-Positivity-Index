from datetime import datetime
import pandas as pd
import praw
from praw.models import MoreComments

class flair_extractor:
    
    
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
            for submission in reddit.subreddit(subreddit).search(query = query,time_filter = "month", limit = None):
                submissions.append(submission)
        
        return submissions
    
    
    def get_all_submissions(self,reddit: praw.reddit,team_flairs: dict):
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
        
        for submission in submissions:
            
            subreddit_name = reddit.Subreddit(submission)
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

