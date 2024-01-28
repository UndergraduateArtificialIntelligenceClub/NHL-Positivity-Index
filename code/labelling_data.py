import os
import json
import random

def label_comment_sentiment(comment:str) -> dict:
    """Given a comment string, displays the comment string and prompts the user to 
    input a label for the comment "Positive", "Neutral", "Negative"

    Args:
        comment (str): A string representing the body of a Reddit comment

    Returns:
        dict: A dictionary containing the comment (str) as the key and the sentiment_label (str)
        as the value. If the user chooses to delete the comment, None is returned
    """
    valid_user_inputs = ["p", "k", "n", "d", "q"]
    
    print(comment)
    sentiment_label = input("Input Sentiment Label: (p) Positive (k) Neutral (n) Negative (d) Delete Comment (q) quit ")
    while sentiment_label not in valid_user_inputs:
        print("Please enter a valid input!")
        sentiment_label = input("Input Sentiment Label: (p) Positive (k) Neutral (n) Negative (d) Delete Comment (q) quit ")
        
    if sentiment_label == "p":
        return "POS"
    
    elif sentiment_label == "k":
        return "NEU"
    
    elif sentiment_label == "n":
        return "NEG"
    
    elif sentiment_label == "q":
        return sentiment_label
    
    else:
        return None

def label_comment_sample(sample: [str]) -> [dict]:
    """Given a list of commments, allows the user to label as many comments as they wish. Returns a list of labelled
    comments and unlabelled comments. All of the comments to the left of j are labelled. j is the index of comment the
    user is currently labelled.

    Args:
        sample [(str)]: A list of comment strings

    Returns:
        [dict, str]: A list of dictionary strings that have been labelled to the left of j and unlabelled comments to the right of j:
        {
            'comment': reddit comment
            'label': sentiment label
        }
    """
    
    for j in range(len(sample)):
        
        # skip over already labelled comments
        if isinstance(sample[j], dict):
            continue
            
        os.system('cls||clear')
        comment = sample[j] 
        comment_label = label_comment_sentiment(comment)
        
        if comment_label == 'q':
            return sample
        
        elif comment_label is None:
            sample.pop(j)
        
        else: 
            sample[j] = {
                'comment': comment,
                'label': comment_label
            }
            
    return sample
    
def get_comment_sample(all_comments: [str], sample_size: int) -> [str]:
    """Given the entire list of comments get a random sample of comments of a desired size

    Args:
        all_comments ([str]): The entire population of Reddit comments in a given time frame
        sample_size (int): The size of the desired sample

    Returns:
        [str]: The sample of comments
    """
    return random.sample(all_comments, sample_size)

def add_labelled_comments_to_json_file(json_file_path: str, labelled_comments: [dict]):
    """Adds labelled comments to a json_file
    Args:
        json_file_path (str): json file path
    """
    with open(json_file_path, 'a', encoding='utf-8') as file:
        json.dump(labelled_comments, file, ensure_ascii=False, indent = 4)
        
def write_labelled_comments_to_json_file(json_file_path: str, labelled_comments: [dict]):
    """Adds labelled comments to a json_file
    Args:
        json_file_path (str): json file path
    """
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(labelled_comments, file, ensure_ascii=False, indent = 4)

    

