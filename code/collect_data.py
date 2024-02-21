import json
names = ['Jacob', 'Alex', 'Arden', 'Heiby', 'Tanmay', 'Yukesh']

new_json = []
for name in names:
    with open(f"data/training_data/updated_comments/{name}_comments_to_label_updated.json","r") as f:
        old_json = json.load(f)
        new_json.extend(old_json)

with open('NHL-SentiComments-5K-TEST.json', 'w') as f:
    json.dump(new_json, f)

