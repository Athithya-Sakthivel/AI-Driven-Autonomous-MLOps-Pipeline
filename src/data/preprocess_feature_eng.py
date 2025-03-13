import os
import json
import yaml
import pandas as pd
from pathlib import Path
from datetime import datetime

# Resolve project root dynamically
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"

# Ensure config file exists
if not CONFIG_PATH.exists():
    raise FileNotFoundError(f"Configuration file not found at {CONFIG_PATH}")

# Load configuration
def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

config = load_config()
DATA_PATHS = config.get("paths", {})

# Define paths
RAW_DATA_DIR = PROJECT_ROOT / Path(DATA_PATHS.get("raw_data", "data/raw"))
PROCESSED_DATA_DIR = PROJECT_ROOT / Path(DATA_PATHS.get("processed_data", "data/processed"))
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Expected schema with corrected data types
EXPECTED_SCHEMA = {
    "title": "string",
    "description": "string",
    "url": "string",
    "publishedAt": "datetime64[ns]",
    "published_year": "int64",
    "published_month": "int64",
    "published_day": "int64",
    "published_weekday": "int64",
    "title_word_count": "int64",
    "description_word_count": "int64"
}

# Load the most recent raw JSON data
def load_raw_data():
    json_files = sorted(RAW_DATA_DIR.glob("newsapi_*.json"), reverse=True)

    if not json_files:
        print("Error: No raw data files found.")
        return None

    latest_file = json_files[0]
    try:
        with open(latest_file, "r") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        print(f"Loaded raw data from {latest_file}")
        return df
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error while loading data: {e}")
        return None

# Clean data
def clean_data(df):
    if df.empty:
        print("Error: Empty dataset after loading. Skipping cleaning.")
        return df

    df.drop_duplicates(subset=["title", "url"], inplace=True)
    df.dropna(subset=["title", "description", "url"], inplace=True)

    # Ensure all text columns are strings
    for col in ["title", "description", "url"]:
        df[col] = df[col].astype(str)

    return df

# Feature engineering
def feature_engineering(df):
    if df.empty:
        print("Error: Empty dataset after cleaning. Skipping feature engineering.")
        return df

    # Convert `publishedAt` to datetime and remove timezone
    df["publishedAt"] = pd.to_datetime(df["publishedAt"], errors="coerce")
    df["publishedAt"] = df["publishedAt"].dt.tz_localize(None)  # Remove timezone

    # Extract date-related features
    df["published_year"] = df["publishedAt"].dt.year.astype("int64", errors="ignore")
    df["published_month"] = df["publishedAt"].dt.month.astype("int64", errors="ignore")
    df["published_day"] = df["publishedAt"].dt.day.astype("int64", errors="ignore")
    df["published_weekday"] = df["publishedAt"].dt.weekday.astype("int64", errors="ignore")

    # Text-based features
    df["title_word_count"] = df["title"].apply(lambda x: len(str(x).split())).astype("int64", errors="ignore")
    df["description_word_count"] = df["description"].apply(lambda x: len(str(x).split())).astype("int64", errors="ignore")

    return df


# Validate data schema
def validate_schema(df):
    if df is None or df.empty:
        print("Error: No data available for validation.")
        return False

    # Check for missing columns
    missing_columns = [col for col in EXPECTED_SCHEMA.keys() if col not in df.columns]
    if missing_columns:
        print(f"Error: Missing columns {missing_columns}")
        return False

    # Validate column data types
    for col, expected_dtype in EXPECTED_SCHEMA.items():
        if col in df.columns:
            actual_dtype = str(df[col].dtype)
            if expected_dtype == "string":
                expected_dtype = "object"
            if actual_dtype != expected_dtype:
                print(f"Error: Column {col} has incorrect type. Expected {expected_dtype}, found {actual_dtype}")
                return False

    print("Data validation passed successfully.")
    return True

# Save processed data
def save_processed_data(df):
    if df.empty:
        print("Error: Processed data is empty. Skipping save.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = PROCESSED_DATA_DIR / f"processed_{timestamp}.csv"
    df.to_csv(save_path, index=False)
    print(f"Processed data saved to {save_path}")

# Main execution
def main():
    df = load_raw_data()
    if df is not None:
        df = clean_data(df)
        df = feature_engineering(df)
        if validate_schema(df):
            save_processed_data(df)

if __name__ == "__main__":
    main()
