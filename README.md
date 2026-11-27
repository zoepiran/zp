# Zoe Piran — personal website

Source for [www.zoepiran.com](https://www.zoepiran.com), served as a static site by GitHub Pages from the root of `main`.

## Preview locally

```sh
python3 -m http.server 8777 --bind 127.0.0.1
```

Open <http://127.0.0.1:8777/>. There is no build step or dependency installation.

## Pages and assets

- `index.html`: two paragraphs introducing the researcher and her research direction. The landing page is text-only.
- `about.html`: biography, portrait, talks and academic organizing. Talk titles are italic. All education and internship details share one paragraph.
- `publications.html`: the complete bibliography in a compact, searchable list. Titles link directly to papers; the single preprint remains in the same list.
- `cv.html`: compatibility redirect to `static/CV_zoepiran.pdf`. Current navigation links open the PDF directly.
- `style.css`: shared typography and responsive layout.
- `site.js`: publication search. Content and navigation also work without JavaScript.
- `static/fonts/`: self-hosted fonts and their licenses.
- `static/img/zp-mark.svg`, `favicon.ico` and `apple-touch-icon.png`: the ZP favicon in browser and touch-icon formats.

The `.md` pages, `conf.py` and Python/Sphinx files belong to the previous site. Existing `ilanit/` and static presentations remain independently accessible. `source/CV_zoepiran.tex` is an earlier website-specific source; it does not reproduce the current supplied PDF. Do not overwrite the PDF by compiling that source.

## Design

Use a compact reading layout: 13px Literata body text, a 14px name, 15px page headings, a 660px left-aligned column, white background, graphite text and blue links. Keep text at this scale on mobile. The About portrait is 64px wide beside the section title on desktop and 56px on mobile. Biography and subsequent sections share one left edge.

Keep navigation ordered About, Publications, CV. There is no separate Research page. Avoid diagrams, cards, decorative arrows, large photos, oversized headings and slide-like sections. Preserve the homepage’s authored punctuation: the semicolon after “scientific autonomy,” “observation (monitoring),” and literal `--->` and `>` characters.

## Verification and publishing

Before publishing, check desktop and phone layouts, local links, publication search, the CV redirect and PDF response. Preserve `CNAME`, `ilanit/`, presentation URLs and the established PDF URL. Verify new bibliographic details against official sources.

The published CV omits the supplied original’s home address, personal phone number and date of birth; citizenship is retained. Keep private contact information and unpublished internal material out of public files. Review any replacement CV before publishing.

GitHub Pages deploys from `main`. Publish only when explicitly requested, then verify the deployment and live pages.
