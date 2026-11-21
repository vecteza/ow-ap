"""Week of 23-29 Nov 2026: posters 09 (Built-In Desk Mini), 10 (review, Laptop Stand),
11 (Kids Learning Tower), 12 (Flat Pack Coffee Table)."""
import os
from PIL import Image, ImageEnhance
os.chdir(os.path.dirname(os.path.abspath(__file__)))
LOGO = open('logo.svg', encoding='utf-8').read()
BASE = """
@font-face{font-family:J;src:url(jak.woff2) format('woff2');font-weight:200 800}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden;font-family:J,sans-serif}
:root{--ink:#141110;--cream:#f4efe8;--red:#d6332a;--mute:#6b625b}
body{background:var(--cream);color:var(--ink)}
.wrap{position:relative;width:1080px;height:1350px;overflow:hidden}
.logo svg{height:40px;width:auto;display:block}
.logo.w svg *{fill:#fff}
.logo.k svg *{fill:var(--ink)}
.pill{display:inline-block;font-size:21px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;padding:10px 20px;border-radius:999px}
.url{font-size:24px;font-weight:700}
.top{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
"""
def doc(css, body):
    return ('<!doctype html><html><head><meta charset="utf-8"><style>' + BASE + css +
            '</style></head><body><div class="wrap">' + body + '</div></body></html>')
posts = {}
os.makedirs('out', exist_ok=True)

# Customer photo crops for poster 10 (keep the stand, drop desktop icons, bottle label and mousepad artwork)
CROPS = {'a': ('reviews/openwood-laptop-stand/hussnainhashmi562-01.jpg', (200, 375, 1300, 1200)),
         'b': ('reviews/openwood-laptop-stand/hussnainhashmi562-02.jpg', (200, 440, 960, 1010)),
         'c': ('reviews/openwood-laptop-stand/hussnainhashmi562-03.jpg', (480, 400, 1400, 1090))}
for k, (f, box) in CROPS.items():
    ImageEnhance.Brightness(Image.open(f).convert('RGB').crop(box).resize((720, 540), Image.LANCZOS)).enhance(1.3).save(f'out/crop10-{k}.jpg', quality=90)

posts['09-small-space-built-in-desk-mini'] = doc("""
.top .pill{background:var(--red);color:#fff}
h1{position:absolute;left:64px;right:64px;top:140px;font-size:98px;font-weight:800;line-height:1.03;letter-spacing:-.04em}
h1 span{color:var(--red)}
.card{position:absolute;left:64px;right:64px;top:362px;height:838px;border-radius:26px;overflow:hidden;background:url(products/built-in-desk-mini/01.png) 50% 22%/cover}
.feat{position:absolute;left:20px;bottom:20px;display:flex;gap:10px}
.feat span{font-size:22px;font-weight:700;padding:10px 16px;border-radius:12px;background:rgba(255,255,255,.95)}
.row{position:absolute;left:64px;right:64px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end}
.row b{font-size:34px;font-weight:800;letter-spacing:-.01em;line-height:1}
.row b i{font-style:normal;font-weight:600;font-size:23px;color:var(--mute);margin-left:14px;letter-spacing:0}
.row .url{font-size:34px;font-weight:800;letter-spacing:-.02em;line-height:1}
""", f"""
<div class="top"><div class="logo k">{LOGO}</div><div class="pill">Small space</div></div>
<h1>Tight corner?<br><span>It fits.</span></h1>
<div class="card"><div class="feat"><span>Fits tight spaces</span><span>No tools needed</span><span>2 sizes</span></div></div>
<div class="row"><b>Built-In Desk Mini<i>200+ sold</i></b><span class="url">openwood.pk</span></div>
""")

posts['10-review-laptop-stand'] = doc("""
body{background:var(--ink);color:var(--cream)}
.ph{position:absolute;left:0;right:0;top:0;height:920px;background:url(products/openwood-laptop-stand/01.png) 0 -70px/1080px auto no-repeat}
.ph::before{content:"";position:absolute;left:0;right:0;top:0;height:200px;background:linear-gradient(180deg,rgba(20,17,16,.72),rgba(20,17,16,0))}
.ph::after{content:"";position:absolute;left:0;right:0;bottom:0;height:170px;background:linear-gradient(180deg,rgba(20,17,16,0),var(--ink))}
.top .pill{border:2px solid rgba(255,255,255,.75);color:#fff}
.cp{position:absolute;right:58px;top:150px;width:262px}
.cp i{display:block;width:248px;height:186px;margin:0 0 16px auto;border:7px solid #fff;border-radius:16px;box-shadow:0 18px 40px rgba(0,0,0,.45);background-size:cover;background-position:50% 50%}
.cp .a{transform:rotate(-3deg);background-image:url(out/crop10-a.jpg)}
.cp .b{transform:rotate(2deg) translateX(-8px);background-image:url(out/crop10-b.jpg)}
.cp .c{transform:rotate(-2deg);background-image:url(out/crop10-c.jpg)}
.cp span{display:block;width:max-content;margin:0 0 20px auto;font-size:19px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;background:var(--red);color:#fff;padding:9px 16px;border-radius:999px}
.q{position:absolute;left:64px;right:64px;bottom:64px}
.stars{font-size:42px;letter-spacing:6px;color:#f5b301}
blockquote{margin-top:18px;font-size:60px;font-weight:700;line-height:1.14;letter-spacing:-.02em;color:#fff}
blockquote em{font-style:normal;color:var(--red)}
.by{margin-top:30px;padding-top:26px;border-top:2px solid rgba(244,239,232,.16);display:flex;justify-content:space-between;align-items:center;font-size:24px;font-weight:600;color:rgba(244,239,232,.7)}
.by b{color:#fff}
.by .url{color:#fff}
""", f"""
<div class="ph"></div>
<div class="top"><div class="logo w">{LOGO}</div><div class="pill">Customer love</div></div>
<div class="cp"><span>Hussnain&rsquo;s photos</span><i class="a"></i><i class="b"></i><i class="c"></i></div>
<div class="q">
 <div class="stars">★★★★★</div>
 <blockquote>&ldquo;Great Product and <em>Fast Delivery</em>.<br>Excellent Service.&rdquo;</blockquote>
 <div class="by"><span><b>Hussnain</b> &middot; Verified buyer &middot; Laptop Stand</span><span class="url">openwood.pk</span></div>
</div>""")

posts['11-kids-learning-tower'] = doc("""
.ph{position:absolute;left:0;right:0;top:0;height:950px;background:url(products/kids-learning-tower/01.png) 50% 60%/cover}
.ph::before{content:"";position:absolute;left:0;right:0;top:0;height:100px;background:linear-gradient(180deg,rgba(244,239,232,.7),rgba(244,239,232,0))}
.ph::after{content:"";position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(180deg,rgba(244,239,232,0),var(--cream))}
.top .pill{background:var(--ink);color:#fff}
.txt{position:absolute;left:64px;right:64px;bottom:60px}
.n{font-size:30px;font-weight:800;color:var(--red);letter-spacing:.02em}
h1{font-size:92px;font-weight:800;line-height:.95;letter-spacing:-.035em;margin-top:8px}
.row{display:flex;justify-content:space-between;align-items:flex-end;margin-top:30px;padding-top:26px;border-top:2px solid rgba(20,17,16,.12)}
.feat{display:flex;gap:10px;flex-wrap:nowrap}
.feat span{font-size:21px;font-weight:700;padding:10px 14px;border-radius:12px;background:#fff;white-space:nowrap}
.shop{font-size:38px;font-weight:800;letter-spacing:-.02em;text-align:right;line-height:1}
.shop small{display:block;font-size:20px;font-weight:700;color:var(--mute);letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px}
""", f"""
<div class="ph"></div>
<div class="top"><div class="logo k">{LOGO}</div><div class="pill">Kids range</div></div>
<div class="txt">
 <div class="n">Kids Learning Tower</div>
 <h1>Little helper.<br>Counter height.</h1>
 <div class="row">
  <div class="feat"><span>Wide, stable base</span><span>Enclosed sides</span><span>No tools needed</span></div>
  <div class="shop"><small>Shop now</small>openwood.pk</div>
 </div>
</div>""")

posts['12-living-room-flat-pack-coffee-table'] = doc("""
body{background:var(--ink);color:#fff}
.ph{position:absolute;left:0;right:0;top:0;height:900px;background:url(products/flat-pack-coffee-table/01.png) 50% 70%/cover}
.ph::before{content:"";position:absolute;left:0;right:0;top:0;height:190px;background:linear-gradient(180deg,rgba(20,17,16,.6),rgba(20,17,16,0))}
.ph::after{content:"";position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(180deg,rgba(20,17,16,0),var(--ink))}
.top .pill{background:var(--red);color:#fff}
.txt{position:absolute;left:64px;right:64px;bottom:60px}
.n{font-size:30px;font-weight:800;color:var(--red);letter-spacing:.02em}
h1{font-size:92px;font-weight:800;line-height:.95;letter-spacing:-.035em;margin-top:8px}
h1 span{color:rgba(255,255,255,.55)}
.row{display:flex;justify-content:space-between;align-items:flex-end;margin-top:30px;padding-top:26px;border-top:2px solid rgba(255,255,255,.16)}
.feat{display:flex;gap:12px;flex-wrap:wrap;max-width:640px}
.feat span{font-size:22px;font-weight:700;padding:10px 16px;border-radius:12px;background:rgba(255,255,255,.1)}
.cta{font-size:28px;font-weight:800;background:#fff;color:var(--ink);padding:16px 26px;border-radius:999px;white-space:nowrap}
""", f"""
<div class="ph"></div>
<div class="top"><div class="logo w">{LOGO}</div><div class="pill">Living room</div></div>
<div class="txt">
 <div class="n">Flat Pack Coffee Table</div>
 <h1>Arrives flat.<br><span>Ready for chai.</span></h1>
 <div class="row">
  <div class="feat"><span>Ships flat-packed</span><span>No tools needed</span><span>Wipes clean</span></div>
  <div class="cta">openwood.pk</div>
 </div>
</div>""")

for k, v in posts.items():
    open(f'out/{k}.html', 'w', encoding='utf-8').write(v.replace('url(out/', 'url(').replace('url(products', 'url(../products').replace('url(jak', 'url(../jak'))
print('\n'.join(posts))
