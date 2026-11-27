# QA report: feature/four-roles-repositioning

Use this as the pull request description. Checked on 27 Nov 2026 with headless Chrome on Windows.

## Checklist (brief, section 9)

- [x] `docs/site-audit.md` written before any change
- [x] All work on `feature/four-roles-repositioning`, nothing deployed, `main` untouched
- [x] Every new or changed section checked at 375 / 768 / 1280px. No horizontal overflow on any page at any width (measured, not just eyeballed). Screenshots are in `docs/screenshots/` on the machine that ran the checks; that folder is git-ignored to keep binaries out of the repo.
- [x] No broken internal links or anchors on the five changed or new pages (script check of every `href`, including `#demo`, `#product`, `#run`, `#pilot`). **Not run:** an external link-checker tool; there is no Node.js or Python on this machine.
- [x] The tax FAQ answer has static text, so it is no longer empty without JavaScript
- [x] Ask Midas examples are labelled "Illustrative example, sample data"
- [x] Every `{{TODO}}` is listed in `docs/placeholders.md` with file and line
- [x] No invented testimonials, logos, certifications, client names or benchmark numbers. Every number the brief did not supply is a `{{TODO}}`.
- [x] No third-party brand assets on `/for/*`. The group is named in plain text only.
- [x] `/for/*` is `noindex, nofollow` (meta tag, plus an `X-Robots-Tag` header on Netlify), missing from the sitemap, and not linked from any page, script or stylesheet
- [ ] **Lighthouse before and after: not run.** No Node.js on this machine, so the CLI is unavailable. Run it in Chrome DevTools or PageSpeed Insights against a preview deploy of this branch and against production, and record both here.
- [x] Keyboard: all new controls are native links, buttons, inputs or `<details>`, so they are reachable by Tab, and a visible focus outline is defined for all of them. New pages have a skip link. **Not done:** a manual tab-through in a real browser.
- [~] Contrast: new text uses a darker orange (`--orange-ink`, #A8520A) that passes AA on the cream background, and eyebrow labels were moved to it. **Pre-existing and unchanged:** white text on the orange buttons (#E07A10, about 2.9:1) and the large gold display numerals do not meet AA. Fixing them means changing brand colours, which needs the owner's call.
- [x] Print stylesheet on `/for/*` gives a clean 3-page A4 PDF (checked with Chrome's print-to-PDF)
- [x] No build step, TypeScript or linter exists. No console errors on any page. The only message in local `file://` testing is the existing service-worker cleanup code, which does not occur over https.

## Lighthouse scores

| | Performance | Accessibility | Best Practices | SEO |
|---|---|---|---|---|
| Before (production) | not measured | not measured | not measured | not measured |
| After (branch preview) | not measured | not measured | not measured | not measured |

## Decisions made without the owner's answer

1. **`/cfo-preview/` assets left where they are.** Three live pages load the logo and dashboard image from there.
2. **Analytics: events only, no tracking script.** The five events are pushed to `window.dataLayer` by `assets/midas.js`. Nothing is sent anywhere until a tag (for example the existing GTM container used by other sites in this repo) is added to the Midas pages.
3. **`docs/` hidden on Netlify** with a redirect in `netlify.toml`. If the domain is served by GitHub Pages instead, `docs/` would be public; move it out of the repo root in that case.
4. **Pain points:** the site had four, not five. The new one was added as the fifth.
5. **Retail use cases are always shown first** in "What should Midas run first?", tagged "Retail groups". The brief asked for this "when the retail audience tab is active", but the site has no audience tabs.
6. **India added as a region** in the market switcher with GST lines marked `{{TODO: confirm}}`. Remove the `in` entry from `REG` in `index.html` if GST is not supported.
7. **Fundraising claims:** the sentence "raised debt and equity across the Gulf, Asia, Africa and the US" was replaced by a `{{TODO}}` for a specific, checkable claim, as the brief asked.
8. **Pilot intent:** pilot buttons set a hidden `intent=pilot` field on the booking form and the email subject becomes "Midas pilot request".
9. **Benchmark page is `noindex`** and out of the sitemap until real data replaces the placeholders. `/retail/` and `/security/` are in the sitemap as the brief asked, but both still contain placeholders.

## Before merging to main

Do not merge while `{{TODO}}` placeholders remain on public pages: they show as yellow chips to visitors. The claim "7 days → 2 minutes" in the hero is qualified with a placeholder for the task definition and links to a benchmark page with no data yet.

## Not done

- Demo video modal: there is no video, so "See a 2-minute run" links to `/benchmark/#run`, which holds a placeholder.
- Old hash URLs in `sitemap.xml` (`/#/investors` and so on) were left alone; `/from-tally/` and `/vs-power-bi/` are still not listed.
