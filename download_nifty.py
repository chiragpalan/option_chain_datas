import os
from datetime import datetime
import pytz
from playwright.sync_api import sync_playwright

# URL
URL = "https://groww.in/options/nifty"

# Make folder
os.makedirs("nifty_chain", exist_ok=True)

# Get IST timestamp
ist = pytz.timezone("Asia/Kolkata")
timestamp = datetime.now(ist).strftime("%d-%m-%Y-%H-%M")
file_path = f"nifty_chain/{timestamp}_nifty50.mhtml"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Go to the page
    page.goto(URL, wait_until="networkidle")

    # Get Chrome DevTools Protocol session
    client = page.context.new_cdp_session(page)

    # Capture MHTML (full single file webpage)
    result = client.send("Page.captureSnapshot", {"format": "mhtml"})

    # Save to .mhtml file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(result["data"])

    browser.close()

print(f"✅ Saved full webpage snapshot: {file_path}")
