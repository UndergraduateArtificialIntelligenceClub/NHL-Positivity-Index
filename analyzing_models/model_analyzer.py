import torch
from transformers import pipeline
import json
import pandas as pd

from google.colab import drive
drive.mount('/content/drive')


# Used to analyze models. Just type the path to the model, the mappings to our labels, and name the model. 
# Run in google colab.  
num_of_models = 2
model_paths = {
    "model_name":['mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis',
                  'ProsusAI/finbert'],
    "label_mappings":[{"positive": "POS", "negative":"NEG", "neutral":"NEU"},
                      {"positive": "POS", "negative":"NEG", "neutral":"NEU"}],
    "name":["model5","model6"]
    }
model_paths = pd.DataFrame(model_paths)

def get_data():

    json_file_path = "/content/drive/MyDrive/NHL-SentiComments-1K-TEST.json"
    with open(json_file_path, 'r', encoding = 'utf-8') as file:
        return json.load(file)

def get_model_results(data,model_path,label_mapping,name):

    sentiment_analysis = pipeline("sentiment-analysis", model= model_path, tokenizer= model_path, max_length=512, truncation=True)

    model_results = pd.DataFrame(columns = ['our label','model label'])
    for i in range(len(data)):
        our_label = data[i]['label']

        model_label = sentiment_analysis(data[i]['comment'])[0]['label']

        new_row = pd.DataFrame({'our label':[data[i]['label']],'model label':[label_mapping[model_label]]})
        model_results = pd.concat([model_results, new_row])

    # Outputs "name.csv" to google drive. 
    model_results.to_csv(f"/content/drive/MyDrive/{name}.csv")


def main():
    data = get_data()

    for i,row in model_paths.iterrows():
        get_model_results(data, model_path= row["model_name"],label_mapping= row["label_mappings"], name = row["name"])

main()