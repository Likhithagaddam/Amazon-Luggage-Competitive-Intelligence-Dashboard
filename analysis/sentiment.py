from textblob import TextBlob
import pandas as pd

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

def analyze_sentiment():
    df = pd.read_csv("data/cleaned_data.csv")

    df["sentiment"] = df["review"].apply(get_sentiment)

    df.to_csv("data/cleaned_data.csv", index=False)

if __name__ == "__main__":
    analyze_sentiment()