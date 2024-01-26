import labelling_data
import comment_preprocessing
import json
import os

def main():
    
    sample_json_file_path = 'testing_sample_5000.json'
    labelled_sample_json_file_path = 'testing_sample_5000_labelled.json'
    
    with open(sample_json_file_path, 'r', encoding='utf-8') as file:
        comments_split_sample = json.load(file)
        
        # Current Sample Number: 14 (Please Change to the number printed when exiting the program,
        # so we don't get duplicates)
        labelling_data.label_comment_samples(comments_split_sample, labelled_sample_json_file_path, 14)
    
    
    
        
if __name__ == "__main__":
    main()
    