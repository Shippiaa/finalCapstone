import pandas as pd
import spacy
from textblob import TextBlob


# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Function to preprocess text
def preprocess_text(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    # Preprocess text
    clean_text = preprocess_text(text)
    # Create a TextBlob object
    analysis = TextBlob(clean_text)
    # Return the polarity and subjectivity
    return analysis.polarity, analysis.subjectivity

# Load the dataset
df = pd.read_csv('amazon_product_reviews.csv')

# Drop rows with missing values in 'review.text' column
df = df.dropna(subset=['reviews.text'])

# Test the sentiment analysis function on sample reviews
sample_reviews = df['reviews.text'].sample(5)
for review in sample_reviews:
    polarity, subjectivity = analyze_sentiment(review)
    print(f"Review: {review}\nPolarity: {polarity}, Subjectivity: {subjectivity}\n")





