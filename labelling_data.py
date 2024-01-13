import os

def label_comment_sentiment(comment:str) -> dict:
    """Given a comment string, displays the comment string and prompts the user to 
    input a label for the comment "Positive", "Neutral", "Negative"

    Args:
        comment (str): A string representing the body of a Reddit comment

    Returns:
        dict: A dictionary containing the comment (str) as the key and the sentiment_label (str)
        as the value. If the user chooses to delete the comment, None is returned
    """
    valid_user_inputs = ["p", "k", "n", "d", "e"]
    
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

def label_multiple_comment_samples(multiple_samples: [[str]], sample_size: int) -> [[str]]

def main():


if __name__ == "__main__":
    main()
            
        
