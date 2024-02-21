from reddit_login import reddit_initializor
from datetime import date
import json
from reddit import CommentsExtractor
reddit_initializor = reddit_initializor()

# Creating datetime objects for 1st February
feb_1 = date(2024, 2, 1)

# Creating datetime objects for 2nd February
feb_15 = date(2024, 2, 2)

reddit = reddit_initializor.get_reddit()

comments_extractor = CommentsExtractor(reddit, feb_1, feb_15)
extracted_comments = comments_extractor.extract_comments()

with open("../data/feb1_to_feb15.json", "w") as f:
    json.dump(extracted_comments, f)
