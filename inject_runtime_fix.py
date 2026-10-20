import os
import re

SITE_DIR = r"d:\daud\sourcecode\scrape 2\planetono\site"

# 1. Inject runtime interception in index.html
index_file = os.path.join(SITE_DIR, "index.html")
with open(index_file, "r", encoding="utf-8") as f:
    html = f.read()

interceptor = """<script>
// Local offline redirector for Storyblok API & assets
(function() {
  const _origFetch = window.fetch;
  window.fetch = function(input, init) {
    let url = typeof input === 'string' ? input : (input && input.url ? input.url : '');
    if (url.includes('api.storyblok.com') || url.includes('/v2/cdn/stories/')) {
      if (url.includes('global')) {
        return _origFetch('/api_storyblok/global.json', init);
      }
      if (url.includes('home')) {
        return _origFetch('/api_storyblok/home.json', init);
      }
    }
    if (url.includes('a.storyblok.com/f/287985154612015/')) {
      const parts = url.split('/');
      const filename = parts[parts.length - 1].split('?')[0];
      return _origFetch('/storyblok_assets/' + filename, init);
    }
    if (url.includes('ljd0bcgtaoiynl4q.public.blob.vercel-storage.com')) {
      const parts = url.split('/');
      const category = parts[parts.length - 2];
      const filename = parts[parts.length - 1];
      return _origFetch('/' + category + '/' + filename, init);
    }
    return _origFetch.apply(this, arguments);
  };
})();
</script>"""

if "Local offline redirector for Storyblok" not in html:
    html = html.replace("<head>", "<head>" + interceptor)
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("Injected fetch interceptor into index.html")

# 2. Rewrite URLs inside local JSON files
for jf in ["home.json", "global.json"]:
    jpath = os.path.join(SITE_DIR, "api_storyblok", jf)
    if os.path.exists(jpath):
        with open(jpath, "r", encoding="utf-8") as f:
            jdata = f.read()
        
        # Replace Storyblok CDN URLs with local /storyblok_assets/
        jdata_new = re.sub(
            r"https://a\.storyblok\.com/f/287985154612015/[^/]+/[^/]+/([a-zA-Z0-9_\-\.]+)",
            r"/storyblok_assets/\1",
            jdata
        )
        if jdata_new != jdata:
            with open(jpath, "w", encoding="utf-8") as f:
                f.write(jdata_new)
            print(f"Patched image paths in {jf}")

print("Runtime fix injection completed!")
