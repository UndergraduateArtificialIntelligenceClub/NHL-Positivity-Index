import json
import random

testing_random_sample = []
with open('clean_december_2023_comments_body.json', 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        testing_random_sample = random.sample(data, 100)
        
with open('testing_sample_100.json', 'w', encoding='utf-8') as file:
        json.dump(testing_random_sample, file, ensure_ascii=False, indent = 4)