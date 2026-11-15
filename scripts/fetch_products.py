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

# --- customer review photos (shown on product pages as <img alt="Customer photo from USER">) ---
ROUT = "kit/reviews"
rindex = []
for p in index:
    try: page = get(p["url"]).decode("utf-8", "replace")
    except Exception as e: print("page fail", p["url"], e); continue
    seen, count = set(), {}
    for tag in re.findall(r"<img[^>]+>", page):
        m = re.search(r'alt="Customer photo from ([^"]+)"', tag); u = re.search(r'src="([^"]+)"', tag)
        if not (m and u) or u.group(1) in seen: continue
        seen.add(u.group(1))
        author = re.sub(r"[^A-Za-z0-9_.-]", "_", html.unescape(m.group(1)))
        thumb = u.group(1); full = re.sub(r"-\d+x\d+(\.\w+)$", r"\1", thumb)
        ext = os.path.splitext(thumb.split("?")[0])[1].lower() or ".jpg"
        count[author] = count.get(author, 0) + 1
        d = os.path.join(ROUT, p["slug"]); os.makedirs(d, exist_ok=True)
        fn = os.path.join(d, f"{author}-{count[author]:02d}{ext}")
        if not os.path.exists(fn):
            data = None
            for src in (full, thumb):
                try: data = get(src); break
                except Exception as e: print("skip", src, e)
            if data is None: continue
            open(fn, "wb").write(data)
        rindex.append({"product_id": p["id"], "slug": p["slug"], "author": html.unescape(m.group(1)), "file": fn})
os.makedirs(ROUT, exist_ok=True)
json.dump(rindex, open(os.path.join(ROUT, "reviews.json"), "w"), indent=1, ensure_ascii=False)
print(len(rindex), "customer review photos")
