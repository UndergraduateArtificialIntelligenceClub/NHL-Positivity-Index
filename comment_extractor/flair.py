import pandas as pd
import praw

class flair_extractor:
    
    
    
    # *** NOTE!!! This function is limited to save time testing. 
    # TODO: Remove limit
    # A method which searches through the subreddits and each flair, and returns the submissions from that flair
    def search_flair(self,reddit: praw.reddit, subreddit: str, flairs: list) -> (list):
        submissions = []
        
        for flair in flairs:
            query = flair + ": "

            # Gets the three most relevent posts from the search of subreddits, and adds them to our list
            for submission in reddit.subreddit(subreddit).search(query = query,time_filter = "month", limit = 10):
                submissions.append(submission)
        
        return submissions
    
    
    # Searches through all the team's different flairs, and returns all the submission to them. 
    def get_all_submissions(self,reddit: praw.reddit,team_flairs: dict):
        
        all_submissions = []
        # Searches through the flairs of each 
        for team_subreddit in team_flairs:            
            submissions = self.search_flair(reddit = reddit, subreddit = team_subreddit, flairs= team_flairs[team_subreddit])
            all_submissions.extend(submissions)

        return all_submissions
    

    # Searches through the submission, and adds all the comments, and likes to a dataframe. 
    def search_submission(self,df: pd.DataFrame, reddit: praw.reddit,submissions: list):
        comment_depth = 2
        
        for submission in submissions:
            submission.comments.replace_more(limit = comment_depth)
            
            # Gets all the comments and adds them to a df. 
            comments = submission.comments.list()
            new_comments = pd.DataFrame({"body":[comment.body for comment in comments],"score":[comment.score for comment in comments]})
            df = pd.concat([df,new_comments])
        return df
        



