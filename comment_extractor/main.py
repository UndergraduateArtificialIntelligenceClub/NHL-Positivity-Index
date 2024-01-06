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
submissions = flairExtractor.extract_flair_comments(reddit= reddit, start_date=)

# Gets the comments from each submission