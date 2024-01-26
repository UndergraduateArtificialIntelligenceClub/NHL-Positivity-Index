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
    valid_user_inputs = ["p", "k", "n", "d"]
    
    print(comment)
    sentiment_label = input("Input Sentiment Label: (p) Positive (k) Neutral (n) Negative (d) Delete Comment ")
    while sentiment_label not in valid_user_inputs:
        print("Please enter a valid input!")
        sentiment_label = input("Input Sentiment Label: (p) Positive (k) Neutral (n) Negative (d) Delete Comment")
        
    if sentiment_label == "p":
        return {comment: "POS"}
    
    elif sentiment_label == "k":
        return {comment: "NEU"}
    
    elif sentiment_label == "n":
        return {comment: "NEG"}
    
    else:
        return None
        
def label_comment_sample(sample: [str]) -> [dict]:
    """Given a list of commments, returns a list of comments with a labelled sentiment

    Args:
        sample [(str)]: A list of comment strings

    Returns:
        [dict]: A list of dictionary strings
    """
    
    labelled_comments = []
    
    for comment in sample:
        os.system('cls||clear') 
        labelled_comment = label_comment_sentiment(comment)
        
        if labelled_comment:
            labelled_comments.append(labelled_comment)
    
    return labelled_comments

def label_comment_samples(multiple_samples: [[str]], json_file_path: str, sample_number = 0) -> [[dict]]:
    """Given a list of samples of comments ([str]) prompts the user to label the comments or to quit
       Adds labelled comments to a JSON file
    Args:
        multiple_samples (str]]): list of samples of comments ([str])
        json_file_path (str): JSON file to add comments to
    Returns:
        [[dict]]: Returns a list of lists of labelled comment dictionaries
    """
    valid_user_inputs = ["y", "e"]
    labelled_comment_samples = []
    
    user_input = input("Would You like to label more comments (y) or exit (e)? ")
    while user_input not in valid_user_inputs:
        print("Please enter a valid input!")
        user_input = input("Would You like to label more comments (y) or exit (e)? ")
        
    while user_input == "y":
        labelled_comments = label_comment_sample(multiple_samples[sample_number])
        sample_number += 1
        add_labelled_comments_to_json_file(json_file_path, labelled_comments)
        user_input = input("Would You like to label more comments (y) or exit (e)? ")
        
    print(f"Your next sample to label is at index: {sample_number}")
    return labelled_comment_samples

def get_comment_sample(all_comments: [str], sample_size: int) -> [str]:
    """Given the entire list of comments get a random sample of comments of a desired size

    Args:
        all_comments ([str]): The entire population of Reddit comments in a given time frame
        sample_size (int): The size of the desired sample

    Returns:
        [str]: The sample of comments
    """
    return random.sample(all_comments, sample_size)

def break_sample_into_smaller_samples(sample: [str], smaller_sample_size: int) -> [[str]]:
    """Given a sample (list) of comment (str) breaks the sample up into smaller samples

    Args:
        sample ([str]): A sample of comments 
        smaller_sample_size (int): How big the smaller samples are 
    Returns:
        [[str]]: A sample of multipl samples 
    """
    return [sample[x:x+smaller_sample_size] for x in range(0, len(sample), smaller_sample_size)]

def add_labelled_comments_to_json_file(json_file_path: str, labelled_comments: [dict]):
    """Adds labelled comments to a json_file
    Args:
        json_file_path (str): json file path
    """
    with open(json_file_path, 'a', encoding='utf-8') as file:
        json.dump(labelled_comments, file, ensure_ascii=False, indent = 4)
        

    

