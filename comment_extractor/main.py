import pandas as pd
import flair, reddit_login

reddit = reddit_login.reddit_initializor().get_reddit()
flairExtractor = flair.flair_extractor()

# Extracts the comments from each of the submissions.
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

submissions = flairExtractor.get_all_submissions(reddit = reddit,team_flairs = teams_and_flairs)
df = pd.DataFrame(columns=["body","score"])
df = flairExtractor.search_submission(df = df, reddit = reddit, submissions= submissions)

print(df.head())
print(df.describe())
print(df.info())
df.to_csv("comment_extractor\small_limit.csv")
