import praw

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
        query = flair + ": "
        for submission in reddit.subreddit(subreddit).search(
            query=query, sort="new", time_filter="all", limit=None
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