from datetime import datetime
import json
from extract_reddit_comments import extract_HockeyMod_comments,extract_flair_comments, extract_user_comments
import reddit_login



def main():
    
    json_file_path = 'december_2023_comments.json'
    no_flair_teams_and_users = {
        "TampaBayLightning": "RandomBoltsFan",
        "winnipegjets": "DylThaGamer",
        "AnaheimDucks": "dahooddawg"
    }
    
    reddit = reddit_login().get_reddit()

    start_date = datetime(2023, 12, 1).date()
    end_date = datetime(2023, 12, 15).date()

    all_HockeyMod_comments = extract_HockeyMod_comments(reddit, start_date, end_date)
    all_no_flair_comments = extract_user_comments(reddit, start_date, end_date, no_flair_teams_and_users)
    all_flaired_comments = extract_flair_comments(reddit = reddit, start_date = start_date, end_date = end_date)
    
    combined_comments = all_HockeyMod_comments.extend(all_no_flair_comments)
    combined_comments = combined_comments.extend(all_flaired_comments)

    with open(json_file_path, 'w') as json_file:
        json.dump(combined_comments, json_file)

if __name__ == "__main__":
    main()