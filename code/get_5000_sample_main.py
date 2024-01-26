import labelling_data
import comment_preprocessing
import json
import random
import os
random.seed(73)

def main():
    
    json_file_path = 'clean_december_2023_comments_body.json'
    
    
    with open('clean_december_2023_comments_body.json', 'r', encoding='utf-8') as file:
        all_comments = json.load(file)
        sample_size = 5000
        split_sample_size = 50
        comment_sample = labelling_data.get_comment_sample(all_comments, sample_size)
        split_comment_sample = labelling_data.break_sample_into_smaller_samples(comment_sample, split_sample_size)
        
    
    sample_json_file_path = 'testing_sample_5000.json'
    with open(sample_json_file_path, 'a', encoding='utf-8') as json_file:
        json.dump(split_comment_sample, json_file)
        
if __name__ == "__main__":
    main()
    