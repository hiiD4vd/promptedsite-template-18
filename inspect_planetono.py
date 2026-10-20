import os
import json
import time
from playwright.sync_api import sync_playwright

OUTPUT_DIR = os.path.abspath(r"d:\daud\sourcecode\scrape 2\planetono")
os.makedirs(OUTPUT_DIR, exist_ok=True)

requests_log = []
responses_log = []

def run():
    target_url = "https://www.planetono.space/"
    print(f"=== Inspecting {target_url} ===")

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

        def on_request(req):
            requests_log.append({
                "url": req.url,
                "method": req.method,
                "resource_type": req.resource_type
            })

        def safe_print(text):
            try:
                print(text)
            except Exception:
                try:
                    print(text.encode("ascii", "replace").decode("ascii"))
                except Exception:
                    pass

        def on_response(res):
            responses_log.append({
                "url": res.url,
                "status": res.status,
                "content_type": res.headers.get("content-type", ""),
                "content_length": res.headers.get("content-length", "")
            })
            safe_print(f"[{res.status}] {res.url[:100]}")

        page.on("request", on_request)
        page.on("response", on_response)
        page.on("console", lambda m: safe_print(f"[Console {m.type}] {m.text}"))

        print("Navigating to page...")
        try:
            page.goto(target_url, wait_until="networkidle", timeout=30000)
        except Exception as e:
            print("Navigation timeout/notice:", e)

        time.sleep(4)

        # Initial Screenshot
        ss_initial = os.path.join(OUTPUT_DIR, "01_initial_load.png")
        page.screenshot(path=ss_initial)
        print(f"Captured {ss_initial}")

        # Save HTML
        html = page.content()
        with open(os.path.join(OUTPUT_DIR, "page.html"), "w", encoding="utf-8") as f:
            f.write(html)

        # Deep Tech Stack & DOM Analysis
        tech_info = page.evaluate("""() => {
            const scripts = Array.from(document.querySelectorAll('script')).map(s => s.src || s.innerText.slice(0, 100));
            const links = Array.from(document.querySelectorAll('link')).map(l => ({rel: l.rel, href: l.href}));
            const canvases = Array.from(document.querySelectorAll('canvas')).map(c => ({
                id: c.id,
                className: c.className,
                w: c.width,
                h: c.height
            }));
            const audios = Array.from(document.querySelectorAll('audio, video')).map(a => ({
                tag: a.tagName,
                src: a.src,
                currentSrc: a.currentSrc
            }));
            const globals = Object.keys(window).filter(k => 
                ['three', 'babylon', 'gsap', 'scrolltrigger', 'locomotive', 'lenis', 'react', 'vue', 'next', 'nuxt', 'howler', 'pixi', 'matter', 'spline'].some(w => k.toLowerCase().includes(w))
            );
            return {
                title: document.title,
                url: window.location.href,
                scriptsCount: scripts.length,
                scripts: scripts.slice(0, 30),
                linksCount: links.length,
                links: links.slice(0, 30),
                canvases,
                audios,
                globals,
                hasWebGL: !!window.WebGLRenderingContext
            };
        }""")

        with open(os.path.join(OUTPUT_DIR, "tech_analysis.json"), "w", encoding="utf-8") as f:
            json.dump(tech_info, f, indent=2)

        # Save network logs
        with open(os.path.join(OUTPUT_DIR, "network_requests.json"), "w", encoding="utf-8") as f:
            json.dump(requests_log, f, indent=2)

        with open(os.path.join(OUTPUT_DIR, "network_responses.json"), "w", encoding="utf-8") as f:
            json.dump(responses_log, f, indent=2)

        # Scroll down to see animations and additional sections
        print("Scrolling page to trigger lazy loading and scroll animations...")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
        time.sleep(2)
        ss_scroll1 = os.path.join(OUTPUT_DIR, "02_scrolled_middle.png")
        page.screenshot(path=ss_scroll1)
        print(f"Captured {ss_scroll1}")

        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        ss_scroll2 = os.path.join(OUTPUT_DIR, "03_scrolled_bottom.png")
        page.screenshot(path=ss_scroll2)
        print(f"Captured {ss_scroll2}")

        # Try clicking any sound toggle or interactive menu button if present
        interactives = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('button, a, [role="button"]')).map(el => ({
                id: el.id,
                className: el.className,
                text: el.innerText.trim(),
                aria: el.getAttribute('aria-label') || ''
            }));
        }""")
        with open(os.path.join(OUTPUT_DIR, "interactive_elements.json"), "w", encoding="utf-8") as f:
            json.dump(interactives, f, indent=2)

        browser.close()
        print("Inspection completed successfully!")

if __name__ == "__main__":
    run()
