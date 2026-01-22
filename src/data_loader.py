import pandas as pd

def load_datasets():
    trader_df = pd.read_csv("data/raw/historical_trader_data.csv")
    sentiment_df = pd.read_csv("data/raw/fear_greed_index.csv")
    return trader_df, sentiment_df
