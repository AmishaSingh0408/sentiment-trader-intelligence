import gdown
import os

# Create directories if not exist
os.makedirs("data/raw", exist_ok=True)

# Google Drive file IDs
HISTORICAL_DATA_ID = "1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs"
FEAR_GREED_ID = "1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf"

# Output paths
HISTORICAL_OUT = "data/raw/historical_trader_data.csv"
FEAR_GREED_OUT = "data/raw/fear_greed_index.csv"

def download_datasets():
    print("Downloading Historical Trader Data...")
    gdown.download(f"https://drive.google.com/uc?id={HISTORICAL_DATA_ID}", HISTORICAL_OUT, quiet=False)

    print("Downloading Fear & Greed Index Data...")
    gdown.download(f"https://drive.google.com/uc?id={FEAR_GREED_ID}", FEAR_GREED_OUT, quiet=False)

    print("✅ All datasets downloaded successfully!")

if __name__ == "__main__":
    download_datasets()
