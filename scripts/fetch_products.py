"""Download OpenWood product data + images from the public WooCommerce Store API into kit/products/."""
import html, json, os, re, urllib.request
BASE = "https://openwood.pk/wp-json/wc/store/v1/products"
OUT = "kit/products"
UA = {"User-Agent": "openwood-social-kit/1.0"}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return r.read()
os.makedirs(OUT, exist_ok=True)
items, page = [], 1
while True:
    batch = json.loads(get(f"{BASE}?per_page=100&page={page}"))
    if not batch: break
    items += batch; page += 1
index = []
for p in items:
    slug = p["slug"]; d = os.path.join(OUT, slug); os.makedirs(d, exist_ok=True)
    files = []
    for i, im in enumerate(p.get("images", [])):
        src = im["src"]; ext = os.path.splitext(src.split("?")[0])[1].lower() or ".jpg"
        fn = os.path.join(d, f"{i+1:02d}{ext}")
        if not os.path.exists(fn):
            try: open(fn, "wb").write(get(src))
            except Exception as e: print("skip", src, e); continue
        files.append(fn)
    strip = lambda h: html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h or "")).strip())
    index.append({"id": p["id"], "name": html.unescape(p["name"]), "slug": slug, "url": p["permalink"],
                  "categories": [c["name"] for c in p.get("categories", [])],
                  "short_description": strip(p.get("short_description")),
                  "images": files})
json.dump(index, open(os.path.join(OUT, "products.json"), "w"), indent=1, ensure_ascii=False)
print(len(index), "products")

# --- temporary probe: how are customer review photos exposed? ---
os.makedirs(os.path.join(OUT, "_probe"), exist_ok=True)
for slug, pid in [("modular-office-table", 17733), ("modular-desk-shelf", 17743)]:
    for name, url in [(f"{slug}.html", f"https://openwood.pk/product/{slug}/"),
                      (f"{slug}-reviews.json", f"https://openwood.pk/wp-json/wc/store/v1/products/reviews?product_id={pid}&per_page=20")]:
        try: open(os.path.join(OUT, "_probe", name), "wb").write(get(url))
        except Exception as e: print("probe fail", url, e)
