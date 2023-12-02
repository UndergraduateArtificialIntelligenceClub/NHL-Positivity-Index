import praw
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.environ["CLIENT_ID"]
SECRET_KEY = os.environ["SECRET_KEY"]
username = os.environ["reddit_username"]
password = os.environ["reddit_password"]

print(CLIENT_ID)

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = SECRET_KEY,
    password = password,
    user_agent = "UAIS",
    username = username
)

# Boston Bruins, New York Islanders, New York Rangers, Philadelphia Flyers
teams = ["BostonBruins", "NewYorkIslanders", "NYRangers", "PhiladelphiaFlyers"]
#for team in teams:
#    subreddit = reddit.subreddit(team)  # replace 'SubredditName' with the name of the subreddit you're interested in
#    print(f"For {team}: -----")
#    # Get the top 5 hot posts
#    for submission in subreddit.top(time_filter="week", limit=5):
#        print(f"Submission: {submission.title}\nTop 10 comments:")

        # Sort the submission's comments by top and then print the top 10
#        submission.comment_sort = 'top'
#        for comment in submission.comments[:10]:
#           print(comment.body)
#        print("\n---\n")
user = reddit.redditor('HockeyMod')

subreddits = set()
for submission in user.submissions.new(limit=50):
    subreddits.add(submission.subreddit.display_name)

print(subreddits)
print(len(subreddits))
