from requests_html import HTMLSession
from datetime import datetime
import pytz
import os

# Create folder if not exists
os.makedirs("nifty_chain", exist_ok=True)

# Get IST time
ist = pytz.timezone("Asia/Kolkata")
now = datetime.now(ist)
filename = now.strftime("%d-%m-%Y-%H-%M_nifty50.html")
filepath = os.path.join("nifty_chain", filename)

# Fetch and render page
session = HTMLSession()
r = session.get("https://groww.in/options/nifty")

# Render JS (headless browser inside requests-html)
r.html.render(timeout=60, sleep=3)   # sleep helps JS finish loading

with open(filepath, "w", encoding="utf-8") as f:
    f.write(r.html.html)

print(f"✅ Saved {filepath}")
