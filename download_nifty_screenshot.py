import os
from datetime import datetime
import pytz
from playwright.sync_api import sync_playwright

def download_nifty_screenshot():
    # Create folder
    folder = "nifty_chain"
    os.makedirs(folder, exist_ok=True)

    # Get IST timestamp
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    filename = now.strftime("%d-%m-%Y-%H-%M") + "_nifty50.png"
    filepath = os.path.join(folder, filename)

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto("https://groww.in/options/nifty", timeout=60000)

        # Wait for data to load
        page.wait_for_timeout(7000)

        # Take full page screenshot
        page.screenshot(path=filepath, full_page=True)
        browser.close()

    print(f"Saved screenshot: {filepath}")


if __name__ == "__main__":
    download_nifty_screenshot()
