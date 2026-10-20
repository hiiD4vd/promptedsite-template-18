import os
import time
from playwright.sync_api import sync_playwright

OUTPUT_DIR = os.path.abspath(r"d:\daud\sourcecode\scrape 2\planetono")

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        print("Navigating to http://localhost:8888/...")
        page.goto("http://localhost:8888/", wait_until="networkidle", timeout=30000)
        time.sleep(2)

        # Click START button
        start_btn = page.locator("button:has-text('START')")
        if start_btn.count() > 0:
            start_btn.first.click()
            time.sleep(3)

        # Take screenshot of rebranded hero & header
        ss_rebrand_hero = os.path.join(OUTPUT_DIR, "rebrand_01_hero.png")
        page.screenshot(path=ss_rebrand_hero)
        print(f"Captured {ss_rebrand_hero}")

        # Scroll down to bottom contacts section
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        ss_rebrand_contacts = os.path.join(OUTPUT_DIR, "rebrand_02_contacts.png")
        page.screenshot(path=ss_rebrand_contacts)
        print(f"Captured {ss_rebrand_contacts}")

        browser.close()
        print("Rebrand verification completed successfully!")

if __name__ == "__main__":
    run()
