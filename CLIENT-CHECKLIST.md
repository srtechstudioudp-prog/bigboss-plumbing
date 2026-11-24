# B&B Big Boss Foundation Repair & Plumbing: preview notes

This is a **design preview**, not a live site. Built 2026-11-24.

## Demo safety (all in place)
- `noindex, nofollow` meta tag on every page, `X-Robots-Tag` header in `vercel.json`, `robots.txt` disallows everything.
- Preview banner at the top of every page and in the footer.
- Quote forms never send anything. Submit shows a "Demo mode" message (`public/assets/script.js`).
- Photos are free-licence **Pexels** placeholders (slab and rebar work, plumbing hands, cracked concrete, Houston houses and skyline), none taken from the company's own pages. People in them are not the client's crew. The section drawing is original. No BBB logo or other trademarks used.
- The logo and favicon are a **concept mark made for the preview**. The client has no logo we could find. At launch use their real logo.

## Facts used and where they came from (public listings)
| Fact | Source | Status |
|---|---|---|
| Phone (832) 659-7540 | BBB profile | verify |
| Business started 17 Mar 2022 | BBB profile | verify |
| BBB Accredited since 7 Mar 2023 | BBB profile | verify (profile also shows "NR" in one place and A+ elsewhere, so no rating letter is shown) |
| 5.0 rating, 21 Google reviews | Birdeye listing of Google reviews | re-check live count at launch |
| Review themes (professional, honest, fair price, hard-working, 3-day job) | same listing, paraphrased, no names | replace with real quotes with permission |
| Hours Mon-Fri 8-5, Sat-Sun 9-5 | Birdeye listing | verify with owner |
| Residential + commercial, categories Foundation Repair / Plumber / Commercial Plumber | BBB profile | verify |

## Must confirm with the owner before launch
1. **Address.** Listings disagree: 9417 Merle St, Houston 77033 (BBB), 3507 Sarah St, Houston 77026 (Birdeye/HomeSquad), and MapQuest shows Dickinson, TX. The site only says "Houston, Texas" until this is settled.
2. **Service list.** Slab leveling, pier and beam, drainage, slab leak, drain and sewer, water heaters, fixtures are *typical trade scope*, not confirmed offerings.
3. **Process steps** (call, inspection, scope and price, repair) and the FAQ answers on pricing, timing, warranty, priority for leaks.
4. **Texas plumbing licence number.** The BBB profile lists none. Plumbing in Texas requires a licence through the State Board of Plumbing Examiners. Show it in the footer once confirmed. Never claim "licensed" until then.
5. **Entity details.** BBB shows "sole proprietorship" but lists three partners. Names are not used on the site.
6. Service area list (neighbourhoods and nearby cities), languages spoken (Spanish?), emergency availability, warranty terms, financing, payment methods.
7. Email address for leads (none found publicly).
8. The domain `bigboss.foundation.plumbing` shown on listings does not resolve right now, so there was no existing site to copy from.

## Real photos
Ask the owner for before/after job photos, crew, trucks, equipment. Replace the files in `public/img/` (same file names, or edit `tools/build.py`).

## Not done yet (because this is a noindex demo)
Full SEO pass: keyword and SERP validation, schema (LocalBusiness etc.), Google Business Profile, citations, humanize and lint gates. Run `/rank-site` at go-live, when the site gets its real domain, real photos and the confirmed facts above. Remove the preview banner, noindex tags, `X-Robots-Tag` and the robots.txt block, and connect the forms to the owner's phone/email, at that point.

## Rebuild
`python tools/build.py` regenerates `public/` (HTML, favicon, robots.txt). CSS and JS live in `public/assets/`. Deploy `public/` as a static site (Vercel).
