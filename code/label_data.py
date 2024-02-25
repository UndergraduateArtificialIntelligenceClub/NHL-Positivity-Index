from transformers import pipeline
from datasets import Dataset
from calc_positivity_score import calc_positivity_score
import json
import torch
import os
from dotenv import load_dotenv
load_dotenv()
current_directory = os.environ["current_directory"]

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model_path = 'cardiffnlp/twitter-roberta-base-sentiment-latest'
classifier = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path, max_length=512, truncation=True)


def classify_text(data: dict) -> dict:
    data["label"] = classifier(data["body"])
    return data


def convert_to_dataset(file_name: str):
    with open(file_name, "r", encoding = 'utf-8') as f:
        content = json.load(f)
    dataset = Dataset.from_list(content)
    return dataset


def label_dataset(dataset):
    classified_data = dataset.map(classify_text, batched=True)
    return classified_data


if __name__ == "__main__":
    content_dataset = convert_to_dataset(
        f'{current_directory}/data/February_data/clean_feb1_to_feb15_data.json'
    )
    labelled_dataset = label_dataset(content_dataset)
    labelled_dataset.to_json(f'{current_directory}/data/February_data/labelled_feb1_to_feb15_data.json')
    positivity_scores,count_scores = calc_positivity_score(labelled_dataset)
    team_scores = {}
    for key in positivity_scores.keys():
        if count_scores[key]!=0:
            team_scores[key] = positivity_scores[key]/count_scores[key]

    with open(f'{current_directory}/data/February_data/team_pos_scores_feb1_to_feb15_data.json', 'w') as fp:
        json.dump(team_scores, fp)