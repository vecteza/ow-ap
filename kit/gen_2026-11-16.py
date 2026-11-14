"""Week of 16-22 Nov 2026: posters 07 (kids study desk) and 08 (review, modular office table)."""
import os
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
"""
def doc(css, body):
    return ('<!doctype html><html><head><meta charset="utf-8"><style>' + BASE + css +
            '</style></head><body><div class="wrap">' + body + '</div></body></html>')
posts = {}

posts['07-kids-study-desk'] = doc("""
.ph{position:absolute;left:0;right:0;top:0;height:940px;background:url(products/kids-study-desk/01.png) 50% 45%/cover}
.ph::before{content:"";position:absolute;left:0;right:0;top:0;height:200px;background:linear-gradient(180deg,rgba(244,239,232,.85),rgba(244,239,232,0))}
.ph::after{content:"";position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(180deg,rgba(244,239,232,0),var(--cream))}
.top{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.top .pill{background:var(--ink);color:#fff}
.txt{position:absolute;left:64px;right:64px;bottom:60px}
.n{font-size:30px;font-weight:800;color:var(--red);letter-spacing:.02em}
h1{font-size:96px;font-weight:800;line-height:.95;letter-spacing:-.035em;margin-top:8px}
.row{display:flex;justify-content:space-between;align-items:flex-end;margin-top:30px;padding-top:26px;border-top:2px solid rgba(20,17,16,.12)}
.feat{display:flex;gap:12px;flex-wrap:wrap;max-width:640px}
.feat span{font-size:22px;font-weight:700;padding:10px 16px;border-radius:12px;background:#fff}
.shop{font-size:44px;font-weight:800;letter-spacing:-.02em;text-align:right;line-height:1}
.shop small{display:block;font-size:20px;font-weight:700;color:var(--mute);letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px}
""", f"""
<div class="ph"></div>
<div class="top"><div class="logo k">{LOGO}</div><div class="pill">Kids range</div></div>
<div class="txt">
 <div class="n">Kids Study Desk</div>
 <h1>A desk of<br>their own.</h1>
 <div class="row">
  <div class="feat"><span>Built-in shelf</span><span>No tools needed</span><span>Sturdy build</span></div>
  <div class="shop"><small>Shop now</small>openwood.pk</div>
 </div>
</div>""")

posts['08-review-modular-office-table'] = doc("""
body{background:var(--ink);color:var(--cream)}
.ph{position:absolute;left:0;right:0;top:0;height:900px;background:url(products/modular-office-table/04.png) 0 63%/172% auto no-repeat}
.ph::before{content:"";position:absolute;left:0;right:0;top:0;height:190px;background:linear-gradient(180deg,rgba(20,17,16,.7),rgba(20,17,16,0))}
.ph::after{content:"";position:absolute;left:0;right:0;bottom:0;height:200px;background:linear-gradient(180deg,rgba(20,17,16,0),var(--ink))}
.top{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.top .pill{border:2px solid rgba(255,255,255,.75);color:#fff}
.q{position:absolute;left:64px;right:64px;bottom:64px}
.stars{font-size:42px;letter-spacing:6px;color:#f5b301}
blockquote{margin-top:18px;font-size:56px;font-weight:700;line-height:1.16;letter-spacing:-.015em;color:#fff}
blockquote em{font-style:normal;color:var(--red)}
.by{margin-top:30px;padding-top:26px;border-top:2px solid rgba(244,239,232,.16);display:flex;justify-content:space-between;align-items:center;font-size:24px;font-weight:600;color:rgba(244,239,232,.7)}
.by b{color:#fff}
.by .url{color:#fff}
""", f"""
<div class="ph"></div>
<div class="top"><div class="logo w">{LOGO}</div><div class="pill">Customer love</div></div>
<div class="q">
 <div class="stars">★★★★★</div>
 <blockquote>&ldquo;The quality and overall finish are <em>outstanding</em>, exactly as shown in the pictures.&rdquo;</blockquote>
 <div class="by"><span><b>Zeeshan</b> &middot; Verified buyer &middot; Modular Office Table</span><span class="url">openwood.pk</span></div>
</div>""")

os.makedirs('out', exist_ok=True)
for k, v in posts.items():
    open(f'out/{k}.html', 'w', encoding='utf-8').write(v.replace('url(', 'url(../'))
