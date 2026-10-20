import os
import time
import json
from playwright.sync_api import sync_playwright

OUTPUT_DIR = os.path.abspath(r"d:\daud\sourcecode\scrape 2\planetono")

def run():
    failed_requests = []
    console_logs = []

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

        def on_req_failed(req):
            failed_requests.append({
                "url": req.url,
                "failure": req.failure
            })

        def on_console(msg):
            console_logs.append({
                "type": msg.type,
                "text": msg.text
            })

        page.on("requestfailed", on_req_failed)
        page.on("console", on_console)

        print("Navigating to http://localhost:8888/...")
        page.goto("http://localhost:8888/", wait_until="networkidle", timeout=30000)
        time.sleep(3)

        # Preloader screenshot
        ss_preloader = os.path.join(OUTPUT_DIR, "local_00_preloader.png")
        page.screenshot(path=ss_preloader)
        print(f"Captured {ss_preloader}")

        # Click START button
        start_btn = page.locator("button:has-text('START')")
        if start_btn.count() > 0:
            print("Clicking START button...")
            start_btn.first.click()
            time.sleep(4)
        else:
            btn_main = page.locator(".button-main")
            if btn_main.count() > 0:
                print("Clicking .button-main...")
                btn_main.first.click()
                time.sleep(4)

        ss_hero = os.path.join(OUTPUT_DIR, "local_01_hero.png")
        page.screenshot(path=ss_hero)
        print(f"Captured {ss_hero}")

        # Scroll to middle section
        page.mouse.wheel(0, 2000)
        time.sleep(2)
        ss_mid = os.path.join(OUTPUT_DIR, "local_02_section2.png")
        page.screenshot(path=ss_mid)
        print(f"Captured {ss_mid}")

        # Scroll further
        page.mouse.wheel(0, 2500)
        time.sleep(2)
        ss_bottom = os.path.join(OUTPUT_DIR, "local_03_section3.png")
        page.screenshot(path=ss_bottom)
        print(f"Captured {ss_bottom}")

        browser.close()

    print("\n--- Verification Summary ---")
    print(f"Failed requests count: {len(failed_requests)}")
    for fr in failed_requests:
        print(f"  [FAILED REQ] {fr['url']} -> {fr['failure']}")

    errors = [c for c in console_logs if c['type'] == 'error']
    print(f"Console errors count: {len(errors)}")
    for err in errors:
        print(f"  [CONSOLE ERROR] {err['text']}")

    with open(os.path.join(OUTPUT_DIR, "local_verification.json"), "w", encoding="utf-8") as f:
        json.dump({
            "failed_requests": failed_requests,
            "console_logs": console_logs
        }, f, indent=2)

if __name__ == "__main__":
    run()
