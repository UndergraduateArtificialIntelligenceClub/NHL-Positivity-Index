import praw
import pandas as pd 
import numpy as np
import string
import unicodedata
import os
from dotenv import load_dotenv
load_dotenv()
current_directory = os.environ["current_directory"]


def search_flair(reddit: praw.reddit, subreddit: str, flairs: list) -> list:
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
        for submission in reddit.subreddit(subreddit).search(
            f'flair:"{flair}"', sort="new", time_filter="all", limit=None
        ):
            submissions.append(submission)

    return submissions


def get_all_flaired_submissions(reddit: praw.reddit, team_flairs: dict):
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
        submissions = search_flair(
            reddit=reddit, subreddit=team_subreddit, flairs=team_flairs[team_subreddit]
        )
        all_submissions.extend(submissions)

    return all_submissions

def clean_title(title: str):
    """
    Given a Reddit title, removes casing, special characters and diacritics
    
    Params: 
        title (str): Reddit title
        
    Returns: cleaned_title (str)
    """
    
    normalized_title = unicodedata.normalize('NFD', title) # Normalize the title to NFD form to separate characters from their diacritical marks

    without_diacritics = ''.join(c for c in normalized_title if unicodedata.category(c) != 'Mn') # Remove diacritics by filtering out characters with category 'Mn' (Mark, nonspacing)

    lowercased_title = without_diacritics.lower().strip()  
    
    special_characters = string.punctuation + "’" + "-"

    translator = str.maketrans('', '', special_characters)

    cleaned_title = lowercased_title.translate(translator)
    
    return cleaned_title

def title_contains_draft_key_words(title:str) -> bool: 
    """
    Given a Reddit title, returns True/False if that title contains a key word related to the 2024
    NHL entry draft (player names, etc.)
    
    Params: 
        title (str): Reddit title
        
    Returns: bool 
    """
    draft_picks_file = f'{current_directory}/data/draft_data/2024_NHL_entry_draft_results.csv'
    
    df = pd.read_csv(draft_picks_file)
    
    DRAFT_PICKS = list(df['Player'])
    
    DRAFT_PICKS = list(map(lambda x: clean_title(x.split('(')[0].strip().lower()), DRAFT_PICKS))
    
    DRAFT_RELEVANT_WORDS = ['draft ', 'pick ', 'select ', 'prospect ', 'Tij '] + DRAFT_PICKS
    
    title = clean_title(title)
    
    return any(draft_keyword in title.lower() for draft_keyword in DRAFT_RELEVANT_WORDS)
    
