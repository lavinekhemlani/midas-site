# Site audit: midascfo.com

Written before any repositioning changes, on branch `feature/four-roles-repositioning` (27 Nov 2026).

## Framework and styling
- Plain static HTML. No framework, no build step, no bundler, no TypeScript or linter.
- The homepage is one file, `index.html`. Its CSS is inline in a `<style>` block, with design tokens as CSS custom properties on `:root` (`--bg`, `--ink`, `--mute`, `--line`, `--gold`, `--orange`, `--green`, plus the glass tokens `--glass`, `--glass2`, `--gedge`, `--gblur`, `--gshadow`).
- Fonts: EB Garamond (headings, `.serif`) and DM Sans (body), from Google Fonts.
- Its JavaScript is also inline: the region switcher (`REG` data for UAE, US, UK, Europe and Australia), scroll reveal (`.rv`) and the demo form (posts to formsubmit.co).
- Sister pages are standalone files with their own inline CSS: `/from-tally/`, `/vs-power-bi/`. Privacy and terms live at `/tech/privacy/` and `/tech/terms/`.
- "Components" don't exist as a concept. Repeated UI is shared CSS classes. Reusable pieces in this project are built as small custom elements in `assets/midas.js`, so other pages can include them with one `<script>` tag.

## Where content lives
- All homepage copy is hard-coded in `index.html`, apart from region-specific text, which lives in the `REG` object in the same file's script.
- No CMS, no JSON or MDX content files.

## Deployment
- `netlify.toml` publishes the repo root (`publish = "."`) and the Ask Midas function in `netlify/functions/ask.mjs` (the only dependency is `@anthropic-ai/sdk`).
- `CNAME` (midascfo.com) and `.nojekyll` are also present, so GitHub Pages is configured too. Which host actually serves the domain should be confirmed.
- Pushes to `main` deploy, so this branch stays off `main`.
- **Because the whole repo root is published, files in `docs/` (this audit and the placeholders list) will be publicly reachable** at midascfo.com/docs/... once merged. Move them or block that path before merging if that matters.

## Asset paths: `/cfo-preview/`
- The homepage, `/from-tally/` and `/vs-power-bi/` all load `cfo-preview/img/logo.svg` and `cfo-preview/img/dashboard.jpg`, and the OG image points to `/cfo-preview/img/dashboard.jpg`.
- `/cfo-preview/index.html` itself is now just a noindex redirect to `/`.
- So the folder is a leftover from the preview stage that the live pages still depend on. **Nothing has been moved.** Waiting on the owner's decision.

## Analytics
- The Midas homepage, `/from-tally/` and `/vs-power-bi/` have **no analytics**.
- Other sites in the same repo (`/tech/`, `/levelup/`, `/HVAC/`) use Google Tag Manager (`GTM-NRKR7RS8`) or gtag. Phase 7 events need the owner to choose before anything is added.

## SEO files
- `sitemap.xml` lists `/` plus hash URLs (`/#/investors` and so on) from an older version, `/mining/` and `/levelup/` pages. None of the newer Midas pages (`/from-tally/`, `/vs-power-bi/`) are in it. Worth cleaning up in Phase 7.
- `robots.txt` allows everything.

## Current homepage sections (in order)
Hero → outcomes stats → "Sound familiar?" (4 pain points) → What makes Midas different (5) → What should Midas run first (9) → Who it's for (6 cards + From Tally / vs Power BI links) → Local markets (region tabs) → Ask Midas chat → How it works (4-layer stack + integrations) → Pilot steps → Team → Pricing (3 tiers) → FAQ → Trust strip → Closing CTA and demo form → Footer.

## Differences from the brief's assumptions
- The pain-points section has **four** items, not five. Phase 3 adds a fifth (the brief calls it the sixth).
- The hero trust row has three items, as the brief expects. They are reworded in Phase 1. The third is set per region by the script, so the brief's UAE wording shows for UAE visitors and each other region keeps its own line.
- The tax FAQ answer isn't missing in the HTML: it is filled in by the region script (`faqTaxA`). It shows empty only without JavaScript. Phase 3 still gives it static text.

## Tooling limits on this machine
- No Node.js or Python, so the Lighthouse CLI and a link-checker can't run here. Lighthouse before/after scores need to come from Chrome DevTools (Lighthouse tab) or PageSpeed Insights on a preview deploy.
- Screenshots are taken with headless Chrome.
