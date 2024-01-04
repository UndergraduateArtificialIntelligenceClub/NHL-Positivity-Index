import pandas as pd
import flair, reddit_login

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

# Creates logs into reddit and creates flair extractor
reddit = reddit_login.reddit_initializor().get_reddit()
flairExtractor = flair.flair_extractor()

# Gets all the submissions which we need to get comments from
submissions = flairExtractor.get_all_submissions(reddit = reddit,team_flairs = teams_and_flairs)

# Gets the comments from each submission
df = pd.DataFrame(columns=['submission_id','comment_id','body','score','date','subreddit'])
df = flairExtractor.search_submission(df = df, reddit = reddit, submissions= submissions)

# Saves it to a JSON file
df.reset_index(drop=True, inplace=True)
df.to_json(r"comment_extractor\flair_data.JSON")
