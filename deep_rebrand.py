import os
import re

SITE_DIR = r"d:\daud\sourcecode\scrape 2\planetono\site"

def deep_rebrand():
    index_file = os.path.join(SITE_DIR, "index.html")
    with open(index_file, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Replace all visible text and serialized Nuxt payload strings
    html = html.replace("Tubik Studio", "PrompTedSite Studio")
    html = html.replace("tubikstudio.com", "promptedsite.com")
    html = html.replace("tubik", "PrompTedSite")
    html = html.replace("Tubik", "PrompTedSite")
    html = html.replace("TUBIK", "PROMPTED")
    html = html.replace("Planetoño", "PrompTedSpace")
    html = html.replace("PLANETOÑO", "PROMPTED SPACE")
    html = html.replace("mail@tubikstudio.com", "contact@promptedsite.com")

    # 2. Add custom CSS override so the rebranded SVG logo is displayed in header & preloader
    logo_override = """<style id="rebrand-logo-override">
.the-header-desktop__logo .the-logo,
.the-header-mobile__logo .the-logo {
  opacity: 1 !important;
  z-index: 10 !important;
}
.the-header-desktop__logo .the-preloader__logo,
.the-header-mobile__logo .the-preloader__logo,
.the-preloader > .the-preloader__logo {
  display: none !important;
}
.the-preloader:before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 320px;
  height: 85px;
  background: url('/images/logo.svg') no-repeat center center;
  background-size: contain;
  z-index: 6;
}
</style>"""

    if "rebrand-logo-override" not in html:
        html = html.replace("</head>", logo_override + "\n</head>")

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("deep_rebrand: index.html updated successfully!")

    # Also check if any JS bundle has baked-in strings
    for root, dirs, files in os.walk(os.path.join(SITE_DIR, "_nuxt")):
        for file in files:
            if file.endswith(".js"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    c = f.read()
                
                c_new = c.replace("mail@tubikstudio.com", "contact@promptedsite.com")
                c_new = c_new.replace("tubikstudio.com", "promptedsite.com")
                if c_new != c:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(c_new)
                    print(f"deep_rebrand: updated strings in JS {file}")

if __name__ == "__main__":
    deep_rebrand()
