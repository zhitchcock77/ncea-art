# The Painting Room

A static NCEA Painting resource site for a New Zealand secondary art classroom.

Open **dist/index.html** directly, or serve `dist` with `python3 -m http.server 8000 --directory dist`.

## Included

- Level 1, 2 and 3 overview pages.
- Nine individual task sheets: 1.2–1.4, 2.2–2.4 and 3.2–3.4.
- 22 artist models: seven contemporary Māori, three other contemporary Aotearoa, five contemporary international and seven historical connections.
- Contemporary models integrated into every task sheet, with practical painting investigations, primary source links and selected artist films.
- Licensed or unrestricted example images, teacher guidance and NZQA sources.
- Twelve 50-minute teacher lesson plans for 1.2, with individual PDFs and a complete 26-page A4 pack.
- A4 printing, optional teacher notes, searchable task library, browser-only working notes and evidence checks.

The finished pages work without JavaScript. JavaScript adds filtering, notes and print controls. Fonts and images are local; external artist and NZQA references require internet access.

## Edit

Edit `content.py` for task content and artist metadata, or `lessons.py` for teacher lesson plans, then run `python3 build.py` to regenerate the 28 HTML pages. Edit `dist/assets/site.css` and `dist/assets/site.js` directly for presentation and interactions. No dependency installation or web build is required. After changing lesson content or print styles, run `node scripts/print-lessons.mjs` to refresh the downloadable PDFs (requires Chromium).

## Assessment reference

Sources checked 22 November 2026. Level 1 uses current Visual Arts standards; Levels 2 and 3 use painting-specific standards. Annual format notes refer to **2026**. Confirm NZQA requirements for the actual assessment year before issuing a task. These are independent teaching resources, not NZQA-approved assessments. Suggested teaching steps, timing and quantities are not assessment thresholds. Full primary references appear on every task sheet and the teacher page.

## Images and fonts

Each reproduced painting has a source and rights link in its caption. Other artist references link to their institution rather than reproduce reserved images. See `dist/assets/provenance.json` for image origins and `dist/assets/FONT-LICENSES.txt` for font licences. No generated art or synthetic student exemplars are used.

## Privacy

Working notes and evidence checks are stored only in the current browser when available. Nothing is submitted by this site. Storage is optional, can be cleared and is not a backup. Clear personal notes when using a shared device.
