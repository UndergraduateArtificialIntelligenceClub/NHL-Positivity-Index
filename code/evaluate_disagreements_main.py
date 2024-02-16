import labelling_data
import comment_preprocessing
import json
import os
import random
import numpy as np

random.seed(73)


        
def main():
    
    names = ['Jacob', 'Alex', 'Arden', 'Heiby', 'Tanmay', 'Yukesh']
    
    users_name = input("What is your first name? ").title()
    while users_name not in names:
        print("Please enter a valid name!")
        users_name = input("What is your first name? ").title()
    comments_to_label_file_path = f'data/training_data/{users_name}_comments_to_label.json'
    disagreements_file_path = f'data/training_data/{users_name}_comments_to_label_disagreements.json'
    updated_comments_file_path = f'data/training_data/{users_name}_comments_to_label_updated.json'
    
    
    with open(comments_to_label_file_path, 'r', encoding='utf-8') as comments_to_label_file, open(disagreements_file_path, 'r', encoding='utf-8') as disagreements_file:
        labelled_comments = json.load(comments_to_label_file)
        disagreements = json.load(disagreements_file)
        updated_comment_labels = labelling_data.evaluate_disagreements(labelled_comments, disagreements)
        labelling_data.write_labelled_comments_to_json_file(updated_comments_file_path, updated_comment_labels)
        
        
if __name__ == "__main__":
    main()
    