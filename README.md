# playandplanpaper.com

The website for the Play & Plan Paper printables shop. Plain static HTML, so it is fast and free to host. Every Buy button goes to the Etsy shop.

## Editing

The pages are built by a script. Change the source files, then rebuild:

- Products: `_build/products.json` (name, short line, Etsy link, description). Product photos go in `img/p/<slug>-1.jpg`, `-2.jpg` and so on. `-1` is the cover.
- Guides (blog posts): `_build/guides.py`
- Page layouts and text: `_build/build.py`
- Styles: `_build/base.css` and `_build/extra.css`

```
python3 _build/build.py
```

This rewrites the HTML, `sitemap.xml`, `robots.txt`, `style.css` and `site.js` in the repository root. Commit the results.

## Hosting (Cloudflare Pages)

Workers & Pages → Create → Pages → Connect to Git → this repository.
Framework preset: None. Build command: leave empty. Build output directory: `/`.
Then go to Custom domains and add `playandplanpaper.com` and `www.playandplanpaper.com`.
