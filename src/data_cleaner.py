def clean_data(trader_df, sentiment_df):
    trader_df = trader_df.dropna(subset=["execution price", "size", "side", "time"])
    sentiment_df = sentiment_df.dropna()

    trader_df["time"] = pd.to_datetime(trader_df["time"])
    sentiment_df["Date"] = pd.to_datetime(sentiment_df["Date"])

    return trader_df, sentiment_df
