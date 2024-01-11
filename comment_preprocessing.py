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
            
            if comment['body'] == '' or comment['body'] == '[removed]' or comment['body'] == '[deleted]':
                continue
            cleaned_comment = clean_comment(comment['body'])
            cleaned_comments.append(cleaned_comment)
            
    return cleaned_comments

def main():
    
    json_file_path = 'december_2023_comments.json'
    cleaned_comments = process_comments(json_file_path)
    
    with open('clean_december_2023_comments_body.json', 'w', encoding='utf-8') as file:
        json.dump(cleaned_comments, file, ensure_ascii=False, indent = 4)
if __name__ == "__main__":
    main()
    