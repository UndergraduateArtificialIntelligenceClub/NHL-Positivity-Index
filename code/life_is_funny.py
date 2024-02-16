from reddit_login import reddit_initializor
from extract_reddit_comments import extract_HockeyMod_comments
from datetime import date
import json

reddit_initializor = reddit_initializor()

# Creating datetime objects for 1st February
feb_1 = date(2024, 2, 1)

# Creating datetime objects for 2nd February
feb_15 = date(2024, 2, 2)

reddit = reddit_initializor.get_reddit()

data = extract_HockeyMod_comments(reddit,feb_1,feb_15)

with open("../data/feb1_to_feb15.json","w") as f:
    json.dump(data,f)

