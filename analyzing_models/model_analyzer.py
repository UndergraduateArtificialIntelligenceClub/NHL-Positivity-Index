from transformers import pipeline
import json
import pandas as pd


num_of_models = 1
model_paths = {
    "model_name":["finiteautomata/bertweet-base-sentiment-analysis"],
    "label_mappings":[{"positive": "POS", "negative":"NEG", "neutral":"NEU"}],
    "model_scores":[0]*num_of_models,
    "name":["model7"]
    }
model_paths = pd.DataFrame(model_paths)

def get_data():

    json_file_path = "NHL-SentiComments-1K-TEST.json"
    with open(json_file_path, 'r', encoding = 'utf-8') as file:
        return json.load(file)

def get_model_results(data,model_path,label_mapping,name):

    sentiment_analysis = pipeline("sentiment-analysis", model= model_path, tokenizer= model_path, max_length=512, truncation=True)
    
    model_results = pd.DataFrame(columns = ['our label','model label'])
    for i in range(len(data)):
        our_label = data[i]['label']

        comment = data[i]['comment']
        try:
            
            model_label = sentiment_analysis(comment)[0]['label']
            
            new_row = pd.DataFrame({'our label':[data[i]['label']],'model label':[label_mapping[model_label]]})
            model_results = pd.concat([model_results, new_row])
        except:
            continue

    model_results.to_csv(f"predictions/{name}.csv")


def main():
    data = get_data()

    for i,row in model_paths.iterrows():
        get_model_results(data, model_path= row["model_name"],label_mapping= row["label_mappings"], name = row["name"])

main()