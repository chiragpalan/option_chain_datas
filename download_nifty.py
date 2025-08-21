import requests
from datetime import datetime
import pytz
import os

def download_nifty_html():
    # Folder name
    folder = "nifty_chain"
    os.makedirs(folder, exist_ok=True)

    # IST timezone
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)

    # File name with timestamp
    filename = now.strftime("%d-%m-%Y-%H-%M") + "_nifty50.html"
    filepath = os.path.join(folder, filename)

    # Target URL
    url = "https://groww.in/options/nifty"
    response = requests.get(url)

    if response.status_code == 200:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Saved: {filepath}")
    else:
        print(f"Failed to fetch URL. Status code: {response.status_code}")


if __name__ == "__main__":
    download_nifty_html()
