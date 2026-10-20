import os
import re
import urllib.request

SITE_DIR = r"d:\daud\sourcecode\scrape 2\planetono\site"

# 1. Download og.png if not present
og_url = "https://a.storyblok.com/f/287985154612015/1200x630/be575015cd/og.png"
og_local = os.path.join(SITE_DIR, "storyblok_assets", "og.png")
if not os.path.exists(og_local):
    print("Downloading og.png...")
    try:
        urllib.request.urlretrieve(og_url, og_local)
        print("og.png downloaded successfully!")
    except Exception as e:
        print("Failed to download og.png:", e)

# 2. Patch fonts/poppins.css
poppins_css = os.path.join(SITE_DIR, "fonts", "poppins.css")
if os.path.exists(poppins_css):
    with open(poppins_css, "r", encoding="utf-8") as f:
        p_content = f.read()
    # Replace gstatic URLs with local font files
    p_content = re.sub(r"https://fonts\.gstatic\.com/s/poppins/v24/([^\"\'\)]+)", r"/fonts/\1", p_content)
    with open(poppins_css, "w", encoding="utf-8") as f:
        f.write(p_content)
    print("poppins.css patched for local font references.")

# 3. Patch index.html
index_html = os.path.join(SITE_DIR, "index.html")
if os.path.exists(index_html):
    with open(index_html, "r", encoding="utf-8") as f:
        html = f.read()

    # Rewrite Storyblok assets in index.html
    html = re.sub(
        r"https://a\.storyblok\.com/f/287985154612015/[^/]+/[^/]+/([a-zA-Z0-9_\-\.]+)(\?[^\"\'\s>]*)?",
        r"/storyblok_assets/\1",
        html
    )

    # In case poppins link is not already there
    if "/fonts/poppins.css" not in html:
        html = html.replace("<head>", "<head><link rel=\"stylesheet\" href=\"/fonts/poppins.css\">")

    with open(index_html, "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html patched.")

# 4. Patch JS bundles for absolute URLs -> relative / local URLs
replacements = [
    (
        "https://ljd0bcgtaoiynl4q.public.blob.vercel-storage.com/",
        "/"
    ),
    (
        "https://unpkg.com/@rive-app/canvas@2.32.2/rive.wasm",
        "/rive/rive.wasm"
    ),
    (
        "https://a.storyblok.com/f/287985154612015/2664x2664/b2b32f1cc1/northern-1.avif",
        "/storyblok_assets/northern-1.avif"
    ),
    (
        "https://a.storyblok.com/f/287985154612015/2664x2664/5dbae2dcc0/southern-1.avif",
        "/storyblok_assets/southern-1.avif"
    )
]

for root, dirs, files in os.walk(os.path.join(SITE_DIR, "_nuxt")):
    for file in files:
        if file.endswith(".js"):
            fpath = os.path.join(root, file)
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            modified = False
            for old_str, new_str in replacements:
                if old_str in content:
                    content = content.replace(old_str, new_str)
                    modified = True
            if modified:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Patched JS: {file}")

print("All patches completed successfully!")
