# Placeholders the owner needs to supply

Every `{{TODO: …}}` on the site is listed here with its file and line. On the page, each one renders as a highlighted, dashed-outline chip (class `todo`) so it can't be missed in review.

## Open items from the brief (section 10)
- [ ] Benchmark: task definition, dataset size, human timings by role, Midas timing, accuracy, screen recording
- [ ] Typical hours per role (CA, analyst, IT/data, CFO) and their source
- [ ] Typical UAE monthly cost of those four roles, and the source
- [ ] Midas starting price, or confirmation to keep pricing hidden
- [ ] Supported tax regimes (UAE VAT and corporate tax, other GCC, India GST?)
- [ ] Supported ERP and POS systems
- [ ] Hosting region and data residency, model and data usage policy, certifications
- [ ] Team names, titles, photos, LinkedIn links, backgrounds; specific fundraising and debt track record
- [ ] Contact email, WhatsApp number, office address
- [ ] Pilot scope and commercials
- [ ] Whether the `/cfo-preview/` asset paths are intended (see `docs/site-audit.md`)

## Placeholders on the site

Generated from the files on 27 Nov 2026. Three shared components in `assets/midas.js` render placeholders wherever they are used: `<four-roles>` (home, /retail, pitch), `<pilot-offer>` (home pricing and FAQ, /retail, pitch) and the `todo()` helper they call.

| File | Line | Placeholder |
|---|---|---|
| index.html | 319 | `{{TODO: task definition}}` |
| index.html | 419 | `{{TODO: illustrative answer}}` |
| index.html | 435 | `{{TODO: list only systems actually supported, e.g. SAP, Oracle, Microsoft Dynamics, LS Retail}}` |
| index.html | 450 | `{{TODO: specific, checkable track record, e.g. "Raised $X of debt and equity for N companies in the UAE, India and the US"}}` |
| index.html | 460 | `{{TODO: photo}}` |
| index.html | 460 | `{{TODO: name}}` |
| index.html | 460 | `{{TODO: title, e.g. Co-founder and CEO}}` |
| index.html | 460 | `{{TODO: one-line background}}` |
| index.html | 460 | `{{TODO: URL}}` |
| index.html | 461 | `{{TODO: photo}}` |
| index.html | 461 | `{{TODO: name}}` |
| index.html | 461 | `{{TODO: title, e.g. Head of Finance}}` |
| index.html | 461 | `{{TODO: one-line background}}` |
| index.html | 461 | `{{TODO: URL}}` |
| index.html | 462 | `{{TODO: photo}}` |
| index.html | 462 | `{{TODO: name}}` |
| index.html | 462 | `{{TODO: title, e.g. Head of Engineering}}` |
| index.html | 462 | `{{TODO: one-line background}}` |
| index.html | 462 | `{{TODO: URL}}` |
| index.html | 467 | `{{TODO: AED range, with source}}` |
| index.html | 467 | `{{TODO: AED, or "a fraction of that"}}` |
| index.html | 480 | `{{TODO: your accountant / our controller team}}` |
| index.html | 481 | `{{TODO: task}}` |
| index.html | 483 | `{{TODO: confirmed answer}}` |
| index.html | 484 | `{{TODO: hosting region, e.g. UAE data residency}}` |
| index.html | 484 | `{{TODO: confirm this sentence is true, or remove it}}` |
| index.html | 493 | `{{TODO}}` |
| index.html | 493 | `{{TODO: only ones actually held}}` |
| index.html | 509 | `{{TODO: contact email}}` |
| index.html | 509 | `{{TODO: WhatsApp click-to-chat link}}` |
| index.html | 514 | `{{TODO: contact email}}` |
| index.html | 514 | `{{TODO: WhatsApp number}}` |
| index.html | 514 | `{{TODO: office address}}` |
| index.html | 527 | `{{TODO: your accountant / our controller team}}` |
| index.html | 531 | `{{TODO: confirm supported tax regimes}}` |
| index.html | 532 | `{{TODO: confirm GST support}}` |
| retail/index.html | 36 | `{{TODO: task definition}}` |
| retail/index.html | 75 | `{{TODO: list only systems actually supported, e.g. SAP, Oracle, Microsoft Dynamics, LS Retail}}` |
| retail/index.html | 85 | `{{TODO: confirmed POS list}}` |
| retail/index.html | 86 | `{{TODO: confirmed answer}}` |
| retail/index.html | 87 | `{{TODO: confirm supported tax regimes}}` |
| benchmark/index.html | 34 | `{{TODO}}` |
| benchmark/index.html | 41 | `{{TODO: plain-language task definition, e.g. month-end close to board pack for N entities}}` |
| benchmark/index.html | 47 | `{{TODO: entities, stores, transactions, period}}` |
| benchmark/index.html | 48 | `{{TODO: steps per role}}` |
| benchmark/index.html | 49 | `{{TODO: who, and how}}` |
| benchmark/index.html | 50 | `{{TODO: the run, from which starting state}}` |
| benchmark/index.html | 51 | `{{TODO: the deliverable both sides had to produce}}` |
| benchmark/index.html | 61 | `{{TODO: ~3 days}}` |
| benchmark/index.html | 61 | `{{TODO}}` |
| benchmark/index.html | 61 | `{{TODO}}` |
| benchmark/index.html | 62 | `{{TODO: ~2 days}}` |
| benchmark/index.html | 62 | `{{TODO}}` |
| benchmark/index.html | 62 | `{{TODO}}` |
| benchmark/index.html | 63 | `{{TODO: ~1.5 days}}` |
| benchmark/index.html | 63 | `{{TODO}}` |
| benchmark/index.html | 63 | `{{TODO}}` |
| benchmark/index.html | 64 | `{{TODO: ~0.5 day}}` |
| benchmark/index.html | 64 | `{{TODO}}` |
| benchmark/index.html | 64 | `{{TODO}}` |
| benchmark/index.html | 65 | `{{TODO: ~7 working days}}` |
| benchmark/index.html | 65 | `{{TODO: ~2 minutes}}` |
| benchmark/index.html | 65 | `{{TODO}}` |
| benchmark/index.html | 77 | `{{TODO: video file, screen recording of a full run with a visible timer}}` |
| benchmark/index.html | 85 | `{{TODO: assumptions about the state of the books}}` |
| benchmark/index.html | 86 | `{{TODO: any other limits of the benchmark}}` |
| security/index.html | 37 | `{{TODO}}` |
| security/index.html | 37 | `{{TODO}}` |
| security/index.html | 38 | `{{TODO: e.g. TLS version, encryption at rest, key handling}}` |
| security/index.html | 39 | `{{TODO: e.g. UAE data residency}}` |
| security/index.html | 39 | `{{TODO}}` |
| security/index.html | 39 | `{{TODO}}` |
| security/index.html | 40 | `{{TODO}}` |
| security/index.html | 40 | `{{TODO: confirm "never used to train models" before publishing}}` |
| security/index.html | 43 | `{{TODO: only certifications actually held, e.g. SOC 2 / ISO 27001, or "in progress" with a date}}` |
| security/index.html | 44 | `{{TODO: security contact email}}` |
| for/wig-8k3vqz/index.html | 56 | `{{TODO: meeting date}}` |
| for/wig-8k3vqz/index.html | 65 | `{{TODO: task definition}}` |
| for/wig-8k3vqz/index.html | 74 | `{{TODO: confirm supported tax regimes}}` |
| for/wig-8k3vqz/index.html | 88 | `{{TODO: suggested scope, e.g. one entity or 10 stores}}` |
| for/wig-8k3vqz/index.html | 102 | `{{TODO: name}}` |
| for/wig-8k3vqz/index.html | 102 | `{{TODO: email}}` |
| for/wig-8k3vqz/index.html | 102 | `{{TODO: number}}` |
| assets/midas.js | 165 | `{{TODO: source, e.g. customer interviews or our benchmark}}` |
| assets/midas.js | 189 | `{{TODO: e.g. 1 entity or up to 10 stores}}` |
| assets/midas.js | 192 | `{{TODO: free / fixed fee credited against the contract}}` |
| assets/midas.js | 133 | `{{TODO: ~3 days}}` (typical time per role, default and retail sets) |
| assets/midas.js | 135 | `{{TODO: ~2 days}}` (typical time per role, default and retail sets) |
| assets/midas.js | 137 | `{{TODO: ~1.5 days}}` (typical time per role, default and retail sets) |
| assets/midas.js | 139 | `{{TODO: ~0.5 day}}` (typical time per role, default and retail sets) |
| assets/midas.js | 143 | `{{TODO: ~3 days}}` (typical time per role, default and retail sets) |
| assets/midas.js | 145 | `{{TODO: ~2 days}}` (typical time per role, default and retail sets) |
| assets/midas.js | 147 | `{{TODO: ~1.5 days}}` (typical time per role, default and retail sets) |
| assets/midas.js | 149 | `{{TODO: ~0.5 day}}` (typical time per role, default and retail sets) |
