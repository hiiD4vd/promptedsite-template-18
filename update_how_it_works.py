import os
import json
import re

SITE_DIR = r"d:\daud\sourcecode\scrape 2\planetono\site"

def update():
    print("=== Updating 'How it works' to 'promptedsite' ===")

    # 1. Update api_storyblok/home.json
    home_file = os.path.join(SITE_DIR, "api_storyblok", "home.json")
    if os.path.exists(home_file):
        with open(home_file, "r", encoding="utf-8") as f:
            home_data = json.load(f)
        
        # update timeline_title
        for sec in home_data.get("story", {}).get("content", {}).get("sections", []):
            if sec.get("id") == "how":
                sec["timeline_title"] = "PROMPTEDSiTE"
                print("home.json: timeline_title updated to 'PROMPTEDSiTE'")
        
        with open(home_file, "w", encoding="utf-8") as f:
            json.dump(home_data, f, ensure_ascii=False, indent=2)

    # 2. Update api_storyblok/global.json
    global_file = os.path.join(SITE_DIR, "api_storyblok", "global.json")
    if os.path.exists(global_file):
        with open(global_file, "r", encoding="utf-8") as f:
            global_data = json.load(f)
        
        for item in global_data.get("story", {}).get("content", {}).get("nav_left", []):
            if "how" in item.get("text", "").lower():
                item["text"] = "PrompTedSite"
                print("global.json: nav_left text updated to 'PrompTedSite'")
        
        with open(global_file, "w", encoding="utf-8") as f:
            json.dump(global_data, f, ensure_ascii=False, indent=2)

    # 3. Update index.html
    index_file = os.path.join(SITE_DIR, "index.html")
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            html = f.read()

        # Update big stepper headline
        html = re.sub(r'HOW\s*iT\s*worKS', 'PROMPTEDSiTE', html, flags=re.IGNORECASE)
        html = re.sub(r'HOW\s*IT\s*WORKS', 'PROMPTEDSiTE', html, flags=re.IGNORECASE)

        # Update nav texts
        html = re.sub(r'How\s+it\s+works', 'PrompTedSite', html)
        html = re.sub(r'how\s+it\s+works', 'promptedsite', html)

        # Also add CSS rule for nav text so if the user expects "promptedsite" in header, it displays clearly
        override_css = """
/* Ensure PrompTedSite nav text is visible */
.the-nav__item[href="#how"] .the-nav__item__text {
  opacity: 1 !important;
  pointer-events: auto !important;
}
.the-nav__item[href="#how"] .the-nav__item__rive {
  display: none !important;
}
"""
        if "Ensure PrompTedSite nav text is visible" not in html:
            html = html.replace("</head>", f"<style>{override_css}</style>\n</head>")

        with open(index_file, "w", encoding="utf-8") as f:
            f.write(html)
        print("index.html updated successfully!")

if __name__ == "__main__":
    update()
