import numpy as np

def engineer_features(df):
    df["trade_value"] = df["execution price"] * df["size"]

    df["pnl"] = df.get("closedPnL", 0)

    df["risk_score"] = df["trade_value"] / (df["leverage"] + 1)

    df["sentiment_binary"] = df["Classification"].apply(
        lambda x: 1 if x == "Greed" else 0
    )

    return df
