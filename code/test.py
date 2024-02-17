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
    
    
    with open(comments_to_label_file_path, 'r', encoding='utf-8') as comments_to_label_file:
        comments_to_label = json.load(comments_to_label_file)
        labelled_data = []
        unlablled_data = []
        for comment in comments_to_label:
            if type(comment) is str:
                print(comment)
                
        
if __name__ == "__main__":
    main()
    