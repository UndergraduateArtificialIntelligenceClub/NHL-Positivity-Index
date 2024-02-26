from transformers import pipeline
from datasets import Dataset
from calc_positivity_score import calc_positivity_score
import json
import torch
import os
from dotenv import load_dotenv
import numpy as np
from constants import SUBREDDIT_MAPPING, LABEL_SCORES
from collections import defaultdict

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
