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

        print("Navigating to https://www.planetono.space/...")
        page.goto("https://www.planetono.space/", wait_until="networkidle", timeout=30000)
        time.sleep(3)

        # Click the START button
        start_btn = page.locator("button:has-text('START')")
        if start_btn.count() > 0:
            print("Clicking START button...")
            start_btn.first.click()
            time.sleep(4)
        else:
            print("START button not found directly, looking for button-main...")
            btn_main = page.locator(".button-main")
            if btn_main.count() > 0:
                btn_main.first.click()
                time.sleep(4)

        ss_after_start = os.path.join(OUTPUT_DIR, "04_after_start_hero.png")
        page.screenshot(path=ss_after_start)
        print(f"Captured {ss_after_start}")

        # Scroll down through the 3D sections
        print("Scrolling through 3D story...")
        for i in range(1, 5):
            page.mouse.wheel(0, 1500)
            time.sleep(1.5)
            ss_step = os.path.join(OUTPUT_DIR, f"05_scroll_step_{i}.png")
            page.screenshot(path=ss_step)
            print(f"Captured {ss_step}")

        browser.close()
        print("Interactive test finished successfully!")

if __name__ == "__main__":
    run()
