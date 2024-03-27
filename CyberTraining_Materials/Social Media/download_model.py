from transformers import pipeline

# This line will trigger the download of the model
pipeline("text-classification", model="finiteautomata/bertweet-base-sentiment-analysis")
pipeline("text-classification", model="tanoManzo/minilm-finetuned-mimic-race-ethnicity-multi-label")

print("Model downloaded successfully.")