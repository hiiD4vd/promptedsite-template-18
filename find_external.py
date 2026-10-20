import os
import glob
import re

SITE_DIR = r"d:\daud\sourcecode\scrape 2\planetono\site"

urls = set()
for root, dirs, files in os.walk(SITE_DIR):
    for file in files:
        if file.endswith((".js", ".css", ".json")):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                matches = re.findall(r"https?://[a-zA-Z0-9_\-\./\?=%&]+", content)
                for m in matches:
                    if not any(x in m for x in ["w3.org", "schema.org"]):
                        urls.add(m)

print(f"Total external URLs found across all JS/CSS/JSON in site: {len(urls)}")
for u in sorted(urls):
    print(u)
