import os
import asyncio
from datetime import datetime
import pytz
from pyppeteer import launch

async def save_page_as_single_file():
    url = "https://groww.in/options/nifty"

    # IST timestamp
    ist = pytz.timezone("Asia/Kolkata")
    timestamp = datetime.now(ist).strftime("%d-%m-%Y-%H-%M")

    # Output path
    output_file = os.path.join("nifty_chain", f"{timestamp}_nifty50.html")
    os.makedirs("nifty_chain", exist_ok=True)

    browser = await launch(headless=True, args=["--no-sandbox"])
    page = await browser.newPage()
    await page.goto(url, {"waitUntil": "networkidle2"})

    # Get full rendered HTML (including dynamic content)
    content = await page.content()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Saved single HTML file at {output_file}")

    await browser.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(save_page_as_single_file())
