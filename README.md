# Zoe Piran — personal website

Source for [www.zoepiran.com](https://www.zoepiran.com), served as a static site by GitHub Pages from the root of `main`.

## Preview locally

```sh
python3 -m http.server 8777 --bind 127.0.0.1
```

Open <http://127.0.0.1:8777/>. There is no dependency installation or build step.

## Edit the site

- `index.html`: research overview, Travis, selected papers, talks, biography and contact.
- `publications.html`: complete bibliography. Each article has a year, author list and `data-kind` (`published` or `preprint`).
- `cv.html`: professional history and a link to the public PDF.
- `style.css`: shared typography, colors and responsive layouts.
- `site.js`: accessible publication search and filters. The content and navigation also work without JavaScript.
- `static/`: self-hosted fonts, scientific illustrations, portrait and downloadable documents.
- `source/CV_zoepiran.tex`: source for `static/CV_zoepiran.pdf`. Compile with `tectonic --outdir static source/CV_zoepiran.tex` or a compatible LaTeX engine. Check all rendered pages after changes.

The `.md` pages, `conf.py` and Python/Sphinx files belong to the previous site setup. They are not the source for the current HTML pages. The existing `ilanit/` presentation and static presentation files remain independently accessible.

## Design

Use the AITHYRA / Travis house style: white canvas, ink text, restrained teal, Geist typography, fine rules, thin scientific line drawings and generous space. Keep the shared header and navigation consistent across all three pages. Avoid ornamental cards, shadows, heavy headings and extra accent colors.

The scientific drawings on the homepage are conceptual illustrations, not experimental results. Bibliographic artwork is reused from the author's presentation assets. See `static/art/README.md` for provenance.

## Check before publishing

- Review all pages on desktop, tablet and a narrow phone.
- Check internal anchors, linked assets, publication search and both filters.
- Keep the bibliography and public CV aligned; verify new citations against their official sources.
- Preserve `CNAME`, `ilanit/`, presentation URLs and the established PDF URL.
- Keep private contact details and unpublished internal material out of public files.

Merging into `main` publishes through the existing GitHub Pages setup. A redesign branch does not change the live site.
