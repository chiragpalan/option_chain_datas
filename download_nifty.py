import os
from datetime import datetime
import pytz
from playwright.sync_api import sync_playwright

def download_nifty_fullhtml():
    folder = "nifty_chain"
    os.makedirs(folder, exist_ok=True)

    # IST timestamp
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    filename = now.strftime("%d-%m-%Y-%H-%M") + "_nifty50.html"
    filepath = os.path.join(folder, filename)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto("https://groww.in/options/nifty", timeout=60000)
        page.wait_for_timeout(7000)  # wait for JS content

        # Get final rendered DOM
        html = page.content()

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

        browser.close()

    print(f"Saved: {filepath}")


if __name__ == "__main__":
    download_nifty_fullhtml()
