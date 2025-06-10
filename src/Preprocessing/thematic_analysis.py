import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("../data/all_bank_reviews.csv")

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Preprocess text
def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

df["processed_review"] = df["review"].apply(preprocess)

# Extract Keywords Using TF-IDF
tfidf = TfidfVectorizer(max_features=50)
keywords = tfidf.fit_transform(df["processed_review"])
df["keywords"] = [", ".join(tfidf.get_feature_names_out())] * len(df)

# Save results
df.to_csv("../data/thematic_analysis.csv", index=False)

print("Thematic analysis completed! Results saved.")