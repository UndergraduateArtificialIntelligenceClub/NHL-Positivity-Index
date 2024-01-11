import json

with open('december_2023_comments.json', 'r') as file:
    data = json.load(file)
    if isinstance(data, dict):
        count = len(data)
        print(count)
    elif isinstance(data, list):
        count = len(data)
        print(count)
