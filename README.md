# The Painting Room

A static NCEA Painting resource site for a New Zealand secondary art classroom.

Open **dist/index.html** directly, or serve `dist` with `python3 -m http.server 8000 --directory dist`.

## Included

- Level 1, 2 and 3 overview pages.
- Nine individual task sheets: 1.2–1.4, 2.2–2.4 and 3.2–3.4, each with suggested artwork sizes, quantities and workbook page ranges.
- 24 artist models: seven contemporary Māori, five other contemporary Aotearoa, five contemporary international and seven historical connections.
- Contemporary models integrated into every task sheet, with practical painting investigations, primary source links and selected artist films.
- Licensed or unrestricted example images, teacher guidance and NZQA sources.
- Twelve 50-minute teacher lesson plans for 1.2, with individual PDFs and a complete 26-page A4 pack.
- A4 printing, optional teacher notes, searchable task library, browser-only working notes and evidence checks.

Student pages work without JavaScript. JavaScript adds filtering, notes, print controls and the teacher login. Fonts and images are local; external artist and NZQA references require internet access.

## Edit

Edit `content.py` for task content and artist metadata, or `lessons.py` for teacher lesson plans, then run `python3 build.py` to regenerate the 28 HTML pages. Edit `dist/assets/site.css` and `dist/assets/site.js` directly for presentation and interactions. No dependency installation or web build is required. After changing lesson content or print styles, run `node scripts/print-lessons.mjs` to refresh the downloadable PDFs (requires Chromium).

## GitHub Pages

Live site: https://zhitchcock77.github.io/ncea-art/

Repository: https://github.com/zhitchcock77/ncea-art

Every push to `main` runs `.github/workflows/deploy-pages.yml`, rebuilds the HTML with `python3 build.py`, and publishes `dist/` to GitHub Pages. You can also run the workflow manually from the repository’s **Actions** tab. Repository **Settings → Pages → Build and deployment → Source** must be set to **GitHub Actions**.

Keep `dist/` in version control: it includes the hand-edited CSS and JavaScript, licensed images and fonts, and generated lesson PDFs. The deployment rebuilds HTML only; after changing lesson content or print styles, refresh the PDFs locally with `node scripts/print-lessons.mjs` and commit them before pushing. All internal links are relative so they work under the `/ncea-art/` project path.

## Teacher access

The teacher page, lesson-plan pages and teacher notes on task sheets require the shared teacher password. The browser compares a SHA-256 hash; the password itself is not stored in the site files. Access is remembered in session storage for the current tab. Use **Lock teacher area** before sharing the tab. If browser storage is unavailable, unlocking still works for the current page.

This is a simple deterrent on a static site. The HTML source and direct PDF URLs remain accessible; it is not suitable for confidential material. Teacher content stays hidden when JavaScript is disabled. To change the password, replace its SHA-256 digest in `dist/assets/teacher-auth.js` and `scripts/print-lessons.mjs`.

## Assessment reference

Sources checked 22 November 2026. Level 1 uses current Visual Arts standards; Levels 2 and 3 use painting-specific standards. Annual format notes refer to **2026**. Confirm NZQA requirements for the actual assessment year before issuing a task. These are independent teaching resources, not NZQA-approved assessments. Suggested teaching steps, timing and quantities are not assessment thresholds. Full primary references appear on every task sheet and the teacher page.

## Images and fonts

Each reproduced painting has a source and rights link in its caption. Other artist references link to their institution rather than reproduce reserved images. See `dist/assets/provenance.json` for image origins and `dist/assets/FONT-LICENSES.txt` for font licences. No generated art or synthetic student exemplars are used.

## Privacy

Working notes and evidence checks are stored only in the current browser when available. Nothing is submitted by this site. Storage is optional, can be cleared and is not a backup. Clear personal notes when using a shared device.
