Build: `python3 build/build.py`. Requires `pandoc` and `node` on PATH;
`npm install` once.

New posts: drop `<slug>.html` + `<slug>.json` (`title`, `date`) into
`src/content/blog/` or `src/content/newsletter/`. The HTML body must be valid
XHTML.

## Math

Posts use `<span class="math inline|display">TEX</span>`. Each expression is
rendered twice: KaTeX HTML for the static page (`build/render_math.js`), MathML
via pandoc for the Atom feed.

Why both: KaTeX HTML looks best in browsers but is unusable in RSS readers,
which don't load external CSS. MathML renders natively everywhere but big
operators come out small. Use the best tool for each renderer.

## Email recaps

- juice roundups/moth-year.html email-out.html --css build/style.css
- create a new email; add an emoji
- right click, inspect element
- replace the emoji's html with the body of email-out.html
- georgia font
