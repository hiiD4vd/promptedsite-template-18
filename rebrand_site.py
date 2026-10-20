import os
import re
import json

SITE_DIR = r"d:\daud\sourcecode\scrape 2\planetono\site"

def rebrand():
    print("=== TAHAP 4: REBRANDING MENYELURUH (PROMPTED SITE) ===")

    # 1. Rebrand api_storyblok/global.json
    global_path = os.path.join(SITE_DIR, "api_storyblok", "global.json")
    if os.path.exists(global_path):
        with open(global_path, "r", encoding="utf-8") as f:
            g_data = json.load(f)
        
        content = g_data.get("story", {}).get("content", {})
        if "email" in content:
            content["email"]["email"] = "contact@promptedsite.com"
            content["email"]["url"] = "mailto:contact@promptedsite.com"
            content["email"]["cached_url"] = "mailto:contact@promptedsite.com"
        
        with open(global_path, "w", encoding="utf-8") as f:
            json.dump(g_data, f, ensure_ascii=False, indent=2)
        print("Rebranded global.json")

    # 2. Rebrand api_storyblok/home.json
    home_path = os.path.join(SITE_DIR, "api_storyblok", "home.json")
    if os.path.exists(home_path):
        with open(home_path, "r", encoding="utf-8") as f:
            h_data = json.load(f)

        content = h_data.get("story", {}).get("content", {})
        # SEO
        if "seo" in content and len(content["seo"]) > 0:
            main_seo = content["seo"][0].get("main", {})
            main_seo["title"] = "PrompTedSpace — Cosmic Fast Food Experience"
            main_seo["description"] = "We tried making this real. NASA said No. So for now, it's just a delicious cosmic dining concept reimagined by PrompTedSite."

        # Sections
        for sec in content.get("sections", []):
            if sec.get("id") == "contacts":
                # update contacts title text
                title_obj = sec.get("title", {})
                sec["title"] = {
                    "type": "doc",
                    "content": [
                        {
                            "type": "paragraph",
                            "attrs": {"textAlign": None},
                            "content": [
                                {"text": "We tried maKing this real. NaSA said nO.", "type": "text", "marks": [{"type": "textStyle", "attrs": {"color": ""}}]}
                            ]
                        },
                        {
                            "type": "paragraph",
                            "attrs": {"textAlign": None},
                            "content": [
                                {"text": "So for nOw, it’s just a deliCiOus Concept", "type": "text", "marks": [{"type": "textStyle", "attrs": {"color": ""}}]}
                            ]
                        },
                        {
                            "type": "paragraph",
                            "attrs": {"textAlign": None},
                            "content": [
                                {"text": "By ", "type": "text", "marks": [{"type": "textStyle", "attrs": {"color": ""}}]},
                                {
                                    "text": "PrompTedSite ",
                                    "type": "text",
                                    "marks": [
                                        {"type": "link", "attrs": {"href": "https://promptedsite.com", "target": "_blank", "linktype": "url"}},
                                        {"type": "textStyle", "attrs": {"color": ""}},
                                        {"type": "underline"}
                                    ]
                                },
                                {"text": "🪐✨", "type": "text", "marks": [{"type": "textStyle", "attrs": {"color": ""}}]}
                            ]
                        }
                    ]
                }
                sec["footer_caption_left"] = {
                    "type": "doc",
                    "content": [
                        {"type": "paragraph", "content": [{"text": "Crafted with Cosmic AI", "type": "text"}]},
                        {"type": "paragraph", "content": [{"text": "by PrompTedSite Studio", "type": "text"}]}
                    ]
                }
                sec["footer_caption_right"] = {
                    "type": "doc",
                    "content": [
                        {"type": "paragraph", "content": [{"text": "PrompTedSpace Concept", "type": "text"}]},
                        {"type": "paragraph", "content": [{"text": "All Galaxies Reserved © 2026", "type": "text"}]}
                    ]
                }

        with open(home_path, "w", encoding="utf-8") as f:
            json.dump(h_data, f, ensure_ascii=False, indent=2)
        print("Rebranded home.json")

    # 3. Rebrand index.html
    index_path = os.path.join(SITE_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()

        html = re.sub(r"<title>.*?</title>", "<title>PrompTedSpace — Cosmic Fast Food Experience</title>", html)
        html = re.sub(r'content="Tubik Studio"', 'content="PrompTedSite Studio"', html)
        html = re.sub(r'content="Tubik"', 'content="PrompTedSite"', html)
        html = re.sub(r'content="Planetoño"', 'content="PrompTedSpace"', html)
        html = re.sub(r'mailto:mail@tubikstudio\.com', 'mailto:contact@promptedsite.com', html)
        html = re.sub(r'https://planetono\.space/', 'http://localhost:8888/', html)
        html = re.sub(r'alt="Planetoño"', 'alt="PrompTedSpace"', html)
        
        # Replace footer texts in index.html SSR markup
        html = html.replace('tubikstudio.com', 'promptedsite.com')
        html = html.replace('Tubik', 'PrompTedSite')

        with open(index_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Rebranded index.html")

    # 4. Generate Rebranded SVG Logo: PROMPTED SPACE (惑星プロンプト)
    logo_svg = """<svg width="340" height="90" viewBox="0 0 340 90" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="120%" height="120%">
      <feDropShadow dx="3" dy="5" stdDeviation="0" flood-color="#000000" flood-opacity="1"/>
    </filter>
  </defs>

  <!-- Outline / 3D Shadow layer -->
  <g filter="url(#shadow)">
    <!-- Main Brand Title: PROMPTED -->
    <text x="170" y="44" 
          font-family="'Futura Passata', 'Poppins', 'Arial Black', sans-serif" 
          font-weight="900" 
          font-size="40" 
          letter-spacing="-1.5" 
          text-anchor="middle" 
          stroke="#000000" 
          stroke-width="8" 
          stroke-linejoin="round"
          fill="#000000">
      PROMPTED
    </text>

    <!-- Sub Brand Title: SPACE -->
    <text x="170" y="76" 
          font-family="'Futura Passata', 'Poppins', 'Arial Black', sans-serif" 
          font-weight="900" 
          font-size="28" 
          letter-spacing="5" 
          text-anchor="middle" 
          stroke="#000000" 
          stroke-width="7" 
          stroke-linejoin="round"
          fill="#000000">
      SPACE
    </text>

    <!-- Star Sparkle Left -->
    <path d="M 28 32 L 33 22 L 38 32 L 48 37 L 38 42 L 33 52 L 28 42 L 18 37 Z" 
          fill="#FFC737" stroke="#000000" stroke-width="3" stroke-linejoin="round" />

    <!-- Star Sparkle Right -->
    <path d="M 302 32 L 307 22 L 312 32 L 322 37 L 312 42 L 307 52 L 302 42 L 292 37 Z" 
          fill="#FFC737" stroke="#000000" stroke-width="3" stroke-linejoin="round" />
  </g>

  <!-- Foreground Fill layer -->
  <!-- Main Title: PROMPTED (Warm Cream #F7F2E5) -->
  <text x="170" y="44" 
        font-family="'Futura Passata', 'Poppins', 'Arial Black', sans-serif" 
        font-weight="900" 
        font-size="40" 
        letter-spacing="-1.5" 
        text-anchor="middle" 
        fill="#F7F2E5">
    PROMPTED
  </text>

  <!-- Sub Title: SPACE (Warm Golden Yellow #FFC737) -->
  <text x="170" y="76" 
        font-family="'Futura Passata', 'Poppins', 'Arial Black', sans-serif" 
        font-weight="900" 
        font-size="28" 
        letter-spacing="5" 
        text-anchor="middle" 
        fill="#FFC737">
    SPACE
  </text>

  <!-- Inner Sparkle Highlights -->
  <circle cx="33" cy="37" r="2.5" fill="#FFFFFF"/>
  <circle cx="307" cy="37" r="2.5" fill="#FFFFFF"/>
</svg>"""

    logo_path = os.path.join(SITE_DIR, "images", "logo.svg")
    with open(logo_path, "w", encoding="utf-8") as f:
        f.write(logo_svg)
    print("Rebranded logo.svg to PROMPTED SPACE design")

    print("\nAll Tahap 4 Rebranding successfully completed!")

if __name__ == "__main__":
    rebrand()
