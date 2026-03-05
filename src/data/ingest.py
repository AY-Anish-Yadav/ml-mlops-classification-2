import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Config
DATASET_SLUG = "parisrohan/credit-score-classification"
RAW_DATA_DIR = Path("data/raw")

def download_dataset():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Downloading dataset: {DATASET_SLUG}")
    subprocess.run([
        "kaggle", "datasets", "download",
        "-d", DATASET_SLUG,
        "-p", str(RAW_DATA_DIR),
        "--unzip"
    ], check=True)
    print(f"Download complete. Files saved to {RAW_DATA_DIR}")

def verify_download():
    files = list(RAW_DATA_DIR.glob("*"))
    if not files:
        raise FileNotFoundError("No files found in data/raw!")
    print("Files downloaded:")
    for f in files:
        print(f"  - {f.name} ({f.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    download_dataset()
    verify_download()