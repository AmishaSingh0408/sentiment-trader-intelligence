from src.data_loader import load_datasets
from src.data_cleaner import clean_data
from src.sentiment_engine import map_sentiment
from src.feature_engineering import engineer_features

def main():
    trader_df, sentiment_df = load_datasets()
    clean_trader, clean_sentiment = clean_data(trader_df, sentiment_df)
    merged_df = map_sentiment(clean_trader, clean_sentiment)
    final_df = engineer_features(merged_df)

    print("Pipeline executed successfully.")
    print(final_df.head())

if __name__ == "__main__":
    main()
