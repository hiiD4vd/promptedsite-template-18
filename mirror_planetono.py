import os
import sys
import json
import urllib.parse
import urllib.request
import re

BASE_DIR = os.path.abspath(r"d:\daud\sourcecode\scrape 2\planetono")
SITE_DIR = os.path.join(BASE_DIR, "site")
os.makedirs(SITE_DIR, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "https://www.planetono.space/"
}

def download_file(url, local_path):
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        return True, "Already exists"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as response:
            data = response.read()
            with open(local_path, "wb") as f:
                f.write(data)
        return True, f"Downloaded {len(data)} bytes"
    except Exception as e:
        return False, str(e)

def run():
    print("=== TAHAP 2: SCRAPING & FULL MIRRORING ===")
    
    # 1. Load captured network responses
    with open(os.path.join(BASE_DIR, "network_responses.json"), "r", encoding="utf-8") as f:
        responses = json.load(f)

    # 2. Add extra known assets like favicons and additional storyblok story
    all_urls = set()
    for r in responses:
        u = r['url']
        if not u.startswith('blob:') and not u.startswith('data:'):
            all_urls.add(u)

    extra_urls = [
        "https://a.storyblok.com/f/287985154612015/96x96/2f0831a892/favicon-96x96.png",
        "https://a.storyblok.com/f/287985154612015/512x512/e75e9fae2c/favicon.svg",
        "https://a.storyblok.com/f/287985154612015/x/2be3bf09eb/favicon.ico",
        "https://a.storyblok.com/f/287985154612015/180x180/838a318026/apple-touch-icon.png",
        "https://www.planetono.space/favicon.ico"
    ]
    all_urls.update(extra_urls)

    mapping = {}
    success_count = 0
    fail_count = 0

    for url in sorted(all_urls):
        parsed = urllib.parse.urlparse(url)
        netloc = parsed.netloc
        path = parsed.path
        if path.startswith("/"):
            path = path[1:]
        
        # Determine local destination
        if netloc in ["www.planetono.space", "planetono.space"]:
            if not path or path == "":
                local_path = os.path.join(SITE_DIR, "index.html")
            else:
                local_path = os.path.join(SITE_DIR, path.replace("/", os.sep))
        elif "storyblok.com" in netloc:
            if "api.storyblok.com" in netloc:
                # Save api response to local api directory
                story_name = path.split("/")[-1] # global or home
                local_path = os.path.join(SITE_DIR, "api_storyblok", f"{story_name}.json")
            else:
                # Storyblok CDN assets (images / favicons)
                filename = os.path.basename(path)
                local_path = os.path.join(SITE_DIR, "storyblok_assets", filename)
        elif "vercel-storage.com" in netloc:
            # sounds / rive
            parts = path.split("/")
            category = parts[0] if parts[0] else parts[1]
            filename = parts[-1]
            local_path = os.path.join(SITE_DIR, category, filename)
        elif "fonts.googleapis.com" in netloc:
            local_path = os.path.join(SITE_DIR, "fonts", "poppins.css")
        elif "fonts.gstatic.com" in netloc:
            filename = os.path.basename(path)
            local_path = os.path.join(SITE_DIR, "fonts", filename)
        elif "unpkg.com" in netloc:
            filename = os.path.basename(path)
            local_path = os.path.join(SITE_DIR, "rive", filename)
        else:
            filename = os.path.basename(path) or "asset"
            local_path = os.path.join(SITE_DIR, "external", filename)

        mapping[url] = os.path.relpath(local_path, SITE_DIR).replace("\\", "/")
        
        # Download
        ok, msg = download_file(url, local_path)
        if ok:
            success_count += 1
            print(f"[{success_count}] OK: {url[:70]} -> {mapping[url]}")
        else:
            fail_count += 1
            print(f"[FAIL] {url} -> {msg}")

    print(f"\nTotal Downloaded: {success_count}, Failed: {fail_count}")

    # Save mapping file
    with open(os.path.join(SITE_DIR, "asset_map.json"), "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2)

if __name__ == "__main__":
    run()
