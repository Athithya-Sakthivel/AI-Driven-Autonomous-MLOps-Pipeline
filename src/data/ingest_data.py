import os
import yaml
import requests
import json
import time
from datetime import datetime
from pathlib import Path

# Resolve project root dynamically
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

config = load_config()
NEWSAPI_CONFIG = config.get("news_api", {})
DATA_PATHS = config.get("paths", {})

def fetch_newsapi_data():
    if not NEWSAPI_CONFIG.get("api_key"):
        print("Error: Missing NewsAPI key in config.yaml.")
        return None

    url = f"{NEWSAPI_CONFIG['base_url']}?q={NEWSAPI_CONFIG['query']}&pageSize={NEWSAPI_CONFIG['max_results']}&language={NEWSAPI_CONFIG['language']}&apiKey={NEWSAPI_CONFIG['api_key']}"
    retries = config.get("agents", {}).get("data_ingestion_agent", {}).get("retries", 3)
    backoff_factor = 5

    for _ in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json().get("articles", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching NewsAPI data: {e}. Retrying in {backoff_factor} seconds...")
            time.sleep(backoff_factor)
    return None

def save_data(data, source):
    if not data:
        print(f"No data fetched from {source}. Skipping save.")
        return

    # Ensure paths are relative to the project root
    save_dir = PROJECT_ROOT / Path(DATA_PATHS.get("raw_data", "data/raw"))
    save_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = save_dir / f"{source}_{timestamp}.json"

    with open(save_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Saved {len(data)} articles from {source} to {save_path}")

def main():
    data = fetch_newsapi_data()
    save_data(data, "newsapi")

if __name__ == "__main__":
    main()
