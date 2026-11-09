# OpenWood social kit

Everything the weekly posting task needs. Posters are 1080x1350 PNG/JPG feed images; Reels are 1080x1920 MP4.

## Brand
- Colours: ink #141110 · cream #f4efe8 · red #d6332a · mute #6b625b
- Font: Plus Jakarta Sans (`jak.woff2`, weights 200–800). Headlines 800, tight letter-spacing (-.04em).
- Logo: `logo.svg` (recolour the fill: ink on light, white on dark).
- Layout reference: `gen.py` (6 finished poster designs). Reuse its `doc()` helper and card/pill styles.

## Rules (from Usman)
- No prices on posters by default. Use social proof ("1,200+ sold"), benefits, "openwood.pk". Prices only when the price itself is the hook (e.g. "Desk upgrades under Rs 3,000"); then check them against the live store.
- Videos/Reels: no watermark overlay; put a ~3 s OpenWood end splash (`reel/splash-template.html`) at the end, with a 0.5 s crossfade and the audio fading out.
- Reels get a 1080x1920 cover (`reel/cover-template.html`); keep text inside the middle 1080x1350 (grid crop).
- Captions: short hook, 2–4 benefit lines, "🛒 openwood.pk", Cash on Delivery line when useful, 6–9 hashtags incl. #openwood. No prices unless it's a price-hook post.
- Assembly visuals: show the golden threaded screw inserts where screws go into wood.
- Never use copyrighted characters/brands in designs.

## Publishing pipeline
1. Render posters to `posters/YYYY-MM/` (JPG, quality ~80).
2. `git push` to main, then use the commit-pinned raw URL:
   `https://raw.githubusercontent.com/vecteza/ow-ap/<commit>/posters/YYYY-MM/<file>.jpg`
3. `social_media_upload(url=…)` → `image_id` (videos return `type: video`).
4. `social_post_create(caption, image_id, networks=["instagram","facebook"], publish_at="YYYY-MM-DD 20:30")`.
   Reels: `type="reel", video_id=…, cover_id=…`; optional `collaborators="username"` (Instagram only).

## Product photos
`img/` holds the product photos available here. The store site can't be reached from the workspace, so new product photos must be added to `img/` (or the task can use `product_id` in `social_post_create` to post a product's main photo as-is).

## Log
`posting-log.md` lists every post scheduled, so products and angles rotate.
