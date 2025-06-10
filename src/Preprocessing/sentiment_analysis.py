import pandas as pd
from transformers import pipeline
from tqdm import tqdm

# Load dataset
df = pd.read_csv("../data/all_bank_reviews.csv")

# Load pre-trained DistilBERT sentiment model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Apply sentiment analysis
tqdm.pandas()
df["sentiment"] = df["review"].progress_apply(lambda x: sentiment_pipeline(x)[0]["label"])
df["sentiment_score"] = df["review"].progress_apply(lambda x: sentiment_pipeline(x)[0]["score"])

# Save results
df.to_csv("../data/sentiment_analysis.csv", index=False)

print("Sentiment analysis completed! Results saved.")