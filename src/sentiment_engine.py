def map_sentiment(trader_df, sentiment_df):
    trader_df["date"] = trader_df["time"].dt.date
    sentiment_df["date"] = sentiment_df["Date"].dt.date

    merged = trader_df.merge(
        sentiment_df[["date", "Classification"]],
        on="date",
        how="left"
    )

    return merged
