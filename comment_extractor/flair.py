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
    

    def search_submission(self,df: pd.DataFrame, reddit: praw.reddit,submissions: list):
        """
        Searches through the submission, and adds the necissary information to a dataframe and returns it. 

        Args:
            df (pd.DataFrame):      The dataframe we are extending
            reddit (praw.reddit):   The reddit api connected to our reddit account
            submissions (list):     A list of all the submissions we need to get comments from

        Returns:
            pd.DataFrame:           A dataframe with all the comments, and their information from the last month. 
        """
        
        
        for submission in submissions:
            submission_date = datetime.utcfromtimestamp(submission.created_utc).date()
            
            # Gets all the comments and adds them to a df. 
            submission.comments.replace_more(limit = 3)
            comments = submission.comments.list()
            
            # Appends each comment to the dataframe
            for comment in comments:
                if isinstance(comment, MoreComments):
                    continue
                
                comment_info = pd.DataFrame([{
                        'submission_id': submission.id,  # id of post
                        'comment_id': comment.id,  # id of comment
                        'body': comment.body,  # comment text
                        'score': comment.score,  # number of upvotes
                        'date': submission_date.strftime('%Y-%m-%d'),  # date comment was posted on 
                        'subreddit': str(comment.subreddit)  # subreddit comment was posted in 
                    }])
                
                df = pd.concat([df,comment_info])
        return df
        



