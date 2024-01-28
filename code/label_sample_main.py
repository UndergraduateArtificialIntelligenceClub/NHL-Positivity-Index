import labelling_data
import comment_preprocessing
import json
import os

def main():
    
    json_file_path = r'data\training_data\comments_to_be_labelled.json'
    
    
    with open(json_file_path, 'r', encoding='utf-8') as file:
        
        comments_to_be_labelled = json.load(file)
        labelled_comments = labelling_data.label_comment_sample(comments_to_be_labelled)
        labelling_data.write_labelled_comments_to_json_file(json_file_path, labelled_comments)
             
if __name__ == "__main__":
    main()
    