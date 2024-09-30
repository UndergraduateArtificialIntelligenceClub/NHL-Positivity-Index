import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import math
# Makes a confusion matrix for each of the models . 
num_of_models = 4
model_paths = {
    "model_name":['cardiffnlp/twitter-roberta-base-sentiment-latest',
                  'distilbert/distilbert-base-uncased-finetuned-sst-2-english',
                  'lxyuan/distilbert-base-multilingual-cased-sentiments-student',
                  'cardiffnlp/twitter-xlm-roberta-base-sentiment',
                  'mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis',
                  'ProsusAI/finbert',
                  "finiteautomata/bertweet-base-sentiment-analysis"],
    "name":["model1","model2","model3","model4","model5","model6", "model7"]
    }

model_paths = pd.DataFrame(model_paths)


for i,model in model_paths.iterrows():
    
    df = pd.read_csv("predictions\\"+model["name"] + ".csv")
    ConfusionMatrixDisplay.from_predictions(df["our label"],df["model label"],cmap = "plasma")
    score = round(accuracy_score(df["our label"],df["model label"]),3)*100
    title = "Accuracy Score: "+ str(score) +"% Model:\n" + model["model_name"]
    
    
    plt.title(title)
    plt.savefig("confusion_matrices\\"+model["name"] + ".jpg", dpi = 600)
    