import re
import json
import os
from dotenv import load_dotenv
load_dotenv()
current_directory = os.environ["current_directory"]

def clean_comment(comment: str) -> str:
    """
    Given a comment removes urls, and unicode characters
    Args:
        comment (str): The Reddit comment that needs cleaning

    Returns: A clean string
    """
    comment = re.sub(r"http\S+", "", comment)
    comment = re.sub(r"www\S+", "", comment)
    comment = comment.replace("\u2019", "'")
    comment = comment.replace("\n", "")
    comment = re.sub(r"!\[gif\]\(giphy\|[^\)]+\)", "", comment, flags=re.IGNORECASE)
    if comment == "" or comment == "[removed]" or comment == "[deleted]":
        return None
    return comment.strip()


def process_comments(json_file_path):
    
    
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for comment in data:
            comment["body"] = clean_comment(comment["body"])
            if comment["body"] is None:
                data.remove(comment)
    return data

if __name__ == "__main__":
    
    cleaned_feb1_to_feb15_data = process_comments(f'{current_directory}/data/February_data/feb1_to_feb15_data.json')
    with open(f'{current_directory}/data/February_data/clean_feb1_to_feb15_data.json', 'w', encoding='utf-8') as file:
        json.dump(cleaned_feb1_to_feb15_data, file, ensure_ascii= False, indent = 4)
            
    