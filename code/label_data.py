from transformers import pipeline
from datasets import Dataset
from calc_positivity_score import calc_positivity_score
import json
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = "finiteautomata/bertweet-base-sentiment-analysis"  # You can choose a different model
classifier = pipeline("sentiment-analysis", model=model, truncation=True, device=device)


def classify_text(data: dict) -> dict:
    data["label"] = classifier(data["body"])
    return data


def convert_to_dataset(file_name: str):
    with open(file_name, "r") as f:
        content = json.load(f)
    dataset = Dataset.from_list(content)
    return dataset


def label_dataset(dataset):
    classified_data = dataset.map(classify_text, batched=True)
    return classified_data


if __name__ == "__main__":
    content_dataset = convert_to_dataset(
        "/home/tanmay-munjal/Downloads/UAIS/NHL-Positivity-Index/data/cleaned_feb1_to_feb15_data.json"
    )
    labelled_dataset = label_dataset(content_dataset)
    positivity_scores,count_scores = calc_positivity_score(labelled_dataset)
    team_scores = {}
    for key in positivity_scores.keys():
        if count_scores[key]!=0:
            team_scores[key] = positivity_scores[key]/count_scores[key]
