import re
import json

def clean_comment(comment: str) -> str:
    """
    Given a comment removes urls, and unicode characters
    Args:
        comment (str): The Reddit comment that needs cleaning
    
    Returns: A clean string
    """
    comment = re.sub(r'http\S+', '', comment)
    comment = re.sub(r'www\S+', '', comment)
    comment = comment.replace('\u2019', "'")
    comment = comment.replace('\n', "")
    comment = re.sub(r'!\[gif\]\(giphy\|[^\)]+\)', '', comment, flags=re.IGNORECASE)
    
    return comment.strip()

def process_comments(json_file_path):
    cleaned_comments = []
    
    with open(json_file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        for comment in data:
            cleaned_comment = clean_comment(comment['body'])
            if cleaned_comment == '' or cleaned_comment == '[removed]' or cleaned_comment == '[deleted]':
                continue
            cleaned_comments.append(cleaned_comment)
            
    return cleaned_comments

