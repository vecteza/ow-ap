"""Generates the 5 regular Instagram posts (1080x1350) as HTML; render.ps1 screenshots them."""
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
.price{font-weight:800;letter-spacing:-.02em}
.price del{font-weight:600;opacity:.5;margin-left:14px;font-size:.55em;letter-spacing:0}
.url{font-size:24px;font-weight:700}
"""

def doc(css, body):
    return ('<!doctype html><html><head><meta charset="utf-8"><style>' + BASE + css +
            '</style></head><body><div class="wrap">' + body + '</div></body></html>')

posts = {}

# 1 — Bestseller spotlight: Built-In Desk
posts['01-bestseller-built-in-desk'] = doc("""
.ph{position:absolute;inset:0;background:url(img/desk1.png) 50% 60%/cover}
.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(244,239,232,.0) 40%,rgba(244,239,232,.9) 66%,var(--cream) 78%)}
.top{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.top .pill{background:var(--ink);color:#fff}
.txt{position:absolute;left:64px;right:64px;bottom:64px}
.n{font-size:30px;font-weight:800;color:var(--red);letter-spacing:.02em}
h1{font-size:104px;font-weight:800;line-height:.95;letter-spacing:-.035em;margin-top:10px}
.row{display:flex;justify-content:space-between;align-items:flex-end;margin-top:34px;padding-top:28px;border-top:2px solid rgba(20,17,16,.12)}
.feat{display:flex;gap:12px;flex-wrap:wrap;max-width:560px}
.feat span{font-size:22px;font-weight:700;padding:10px 16px;border-radius:12px;background:#fff}
.price{font-size:48px;text-align:right;line-height:1}
.price small{display:block;font-size:20px;font-weight:700;color:var(--mute);letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px}
""", f"""
<div class="ph"></div>
<div class="top"><div class="logo k">{LOGO}</div><div class="pill">Bestseller</div></div>
<div class="txt">
 <div class="n">1,200+ sold</div>
 <h1>The Built-In<br>Desk</h1>
 <div class="row">
  <div class="feat"><span>Tools included</span><span>Easy assembly</span><span>Cash on Delivery</span></div>
  <div class="price"><small>Shop now</small>openwood.pk</div>
 </div>
</div>""")

# 2 — Customer review (verified buyer, Built-In Desk)
posts['02-review-built-in-desk'] = doc("""
body{background:var(--ink);color:var(--cream)}
.ph{position:absolute;left:0;right:0;bottom:0;height:560px;background:url(img/desk2.png) 50% 55%/cover}
.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,var(--ink) 0%,rgba(20,17,16,.15) 45%,rgba(20,17,16,0) 100%)}
.top{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.top .pill{border:2px solid rgba(244,239,232,.6);color:#fff}
.q{position:absolute;left:64px;right:64px;top:190px}
.stars{font-size:46px;letter-spacing:6px;color:#f5b301}
.mark{font-size:200px;line-height:.6;color:var(--red);font-weight:800;height:90px;margin-top:30px}
blockquote{font-size:56px;font-weight:700;line-height:1.18;letter-spacing:-.015em;color:#fff}
blockquote em{font-style:normal;color:var(--red)}
.by{margin-top:36px;font-size:24px;font-weight:600;color:rgba(244,239,232,.7)}
.by b{color:#fff}
""", f"""
<div class="ph"></div>
<div class="top"><div class="logo w">{LOGO}</div><div class="pill">Customer love</div></div>
<div class="q">
 <div class="stars">★★★★★</div>
 <div class="mark">&ldquo;</div>
 <blockquote>So easy to set up &mdash; it took me <em>barely 5 minutes</em>. All the tools came with it, and the quality and sturdiness is amazing.</blockquote>
 <div class="by"><b>Verified buyer</b> &middot; Built-In Desk</div>
</div>""")

# 3 — Small desk upgrades
cards = [('img/notebook.png', '50% 60%', 'Notebook Stand', '1,500+ sold'),
         ('img/monitor.jpg', '50% 40%', 'Monitor Stand 2.0', '500+ sold'),
         ('img/phone.jpg', '50% 55%', 'Mobile Phone Stand', '2,500+ sold')]
cells = ''.join(f'<div class="c"><div class="im" style="background-image:url({u});background-position:{p}"></div><div class="cap"><b>{n}</b><span>{pr}</span></div></div>' for u, p, n, pr in cards)
posts['03-small-desk-upgrades'] = doc("""
.top{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.top .url{color:var(--mute)}
h1{position:absolute;left:64px;right:64px;top:150px;font-size:86px;font-weight:800;line-height:.98;letter-spacing:-.035em}
h1 span{color:var(--red)}
.grid{position:absolute;left:64px;right:64px;top:380px;bottom:64px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:20px}
.c{background:#fff;border-radius:22px;overflow:hidden;display:flex;flex-direction:column}
.im{flex:1;background-size:cover}
.cap{display:flex;justify-content:space-between;align-items:center;padding:18px 22px;gap:10px}
.cap b{font-size:23px;font-weight:800;line-height:1.15}
.cap span{font-size:24px;font-weight:800;color:var(--red);white-space:nowrap}
.cta{background:var(--ink);color:#fff;border-radius:22px;display:flex;flex-direction:column;justify-content:space-between;padding:34px}
.cta b{font-size:46px;line-height:1.05;letter-spacing:-.02em}
.cta span{font-size:24px;font-weight:700;color:rgba(255,255,255,.75)}
.cta i{font-style:normal;display:inline-block;margin-top:14px;background:#fff;color:var(--ink);padding:14px 22px;border-radius:999px;font-size:22px;font-weight:800}
""", f"""
<div class="top"><div class="logo k">{LOGO}</div><div class="url">openwood.pk</div></div>
<h1>Small upgrades,<br><span>big difference.</span></h1>
<div class="grid">{cells}
 <div class="cta"><b>Small change,<br>better setup.</b><div><span>Desk accessories</span><br><i>Shop at openwood.pk</i></div></div>
</div>""")

# 4 — Modular Desk Shelf: lift your screen
posts['04-modular-desk-shelf'] = doc("""
body{background:#e9e9ea}
.ph{position:absolute;left:0;right:0;top:330px;bottom:150px;background:url(img/deskshelf.png) 50% 50%/cover no-repeat;-webkit-mask:linear-gradient(180deg,transparent 0,#000 12%,#000 88%,transparent 100%)}
.top{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.top .pill{background:var(--red);color:#fff}
h1{position:absolute;left:64px;right:64px;top:150px;font-size:96px;font-weight:800;line-height:.95;letter-spacing:-.04em}
h1 span{color:var(--mute)}
.bar{position:absolute;left:64px;right:64px;bottom:64px;background:var(--ink);color:#fff;border-radius:24px;padding:30px 34px;display:flex;justify-content:space-between;align-items:center;gap:20px}
.bar b{display:block;font-size:34px;letter-spacing:-.01em}
.bar span{font-size:22px;font-weight:600;color:rgba(255,255,255,.7)}
.price{font-size:54px;white-space:nowrap}
""", f"""
<div class="ph"></div>
<div class="top"><div class="logo k">{LOGO}</div><div class="pill">580+ sold</div></div>
<h1>Lift your screen.<br><span>Free your desk.</span></h1>
<div class="bar"><div><b>Modular Desk Shelf</b><span>Monitor riser with room underneath</span></div><div class="price" style="font-size:30px;background:#fff;color:var(--ink);padding:16px 26px;border-radius:999px">openwood.pk</div></div>
""")

# 5 — Small space? Go vertical (wall range)
posts['05-go-vertical-wall-range'] = doc("""
.top{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.top .url{color:var(--mute)}
h1{position:absolute;left:64px;right:64px;top:150px;font-size:92px;font-weight:800;line-height:.95;letter-spacing:-.04em}
h1 span{color:var(--red)}
.sub{position:absolute;left:64px;top:345px;font-size:28px;font-weight:600;color:var(--mute)}
.g{position:absolute;left:64px;right:64px;top:420px;bottom:64px;display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:1fr 1fr;gap:20px}
.c{position:relative;border-radius:22px;overflow:hidden;background-size:cover}
.c.big{grid-row:1 / span 2}
.c .tag{position:absolute;left:16px;right:16px;bottom:16px;background:rgba(255,255,255,.94);border-radius:14px;padding:14px 18px;display:flex;justify-content:space-between;align-items:center;gap:10px}
.c .tag b{font-size:21px;font-weight:800;line-height:1.15}
.c .tag span{font-size:22px;font-weight:800;color:var(--red);white-space:nowrap}
""", f"""
<div class="top"><div class="logo k">{LOGO}</div><div class="url">openwood.pk</div></div>
<h1>Small space?<br><span>Go vertical.</span></h1>
<div class="sub">Wall-mounted storage that frees up the floor.</div>
<div class="g">
 <div class="c big" style="background-image:url(img/wallshelf.png);background-position:50% 30%"><div class="tag"><b>Minimal Wall-Mounted Shelf</b></div></div>
 <div class="c" style="background-image:url(img/keys.png);background-position:60% 45%"><div class="tag"><b>Shelf with Keys Hanger</b></div></div>
 <div class="c" style="background-image:url(img/clothes.png);background-position:50% 25%"><div class="tag"><b>Clothes Hanger</b></div></div>
</div>""")

# 6 — Under Desk Cable Management Tray
posts['06-cable-tray'] = doc("""
body{background:var(--ink);color:#fff}
.ph{position:absolute;left:0;right:0;top:400px;height:640px;background:url(img/cable.png) 50% 0/2000px auto no-repeat}
.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,var(--ink) 0%,rgba(20,17,16,0) 18%,rgba(20,17,16,0) 82%,var(--ink) 100%)}
.top{position:absolute;top:56px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}
.top .pill{background:var(--red);color:#fff}
h1{position:absolute;left:64px;right:64px;top:150px;font-size:96px;font-weight:800;line-height:.95;letter-spacing:-.04em}
h1 span{color:var(--red)}
.bar{position:absolute;left:64px;right:64px;bottom:64px;display:flex;justify-content:space-between;align-items:flex-end;gap:20px}
.bar b{display:block;font-size:36px;letter-spacing:-.01em}
.bar span{font-size:23px;font-weight:600;color:rgba(255,255,255,.7)}
.feat{display:flex;gap:10px;margin-top:18px}
.feat i{font-style:normal;font-size:21px;font-weight:700;padding:9px 15px;border-radius:12px;background:rgba(255,255,255,.1)}
.cta{font-size:28px;font-weight:800;background:#fff;color:var(--ink);padding:16px 26px;border-radius:999px;white-space:nowrap}
""", f"""
<div class="ph"></div>
<div class="top"><div class="logo w">{LOGO}</div><div class="pill">300+ sold</div></div>
<h1>Hide the<br><span>cable chaos.</span></h1>
<div class="bar"><div><b>Under Desk Cable Tray</b><span>Holds power strips, chargers &amp; cables</span><div class="feat"><i>Screws onto any desk</i><i>Ventilated steel</i></div></div><div class="cta">openwood.pk</div></div>
""")

os.makedirs('html', exist_ok=True)
for k, v in posts.items():
    open(f'{k}.html', 'w', encoding='utf-8').write(v)
print('\n'.join(posts))
