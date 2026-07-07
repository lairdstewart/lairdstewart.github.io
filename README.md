## Usage

New posts: drop `<slug>.html` + `<slug>.json` (`title`, `date`) into
`src/content/blog/` or `src/content/newsletter/`. The HTML body must be valid
XHTML. Use `<span class="math display">` and `<span class="math inline">` for
math equations.

Build: `python3 build/build.py`. Requires `pandoc` and `node` on PATH;
`npm install` once.

Run: ./build/server.sh

## Math

Posts use `<span class="math inline|display">TEX</span>`. Each expression is
rendered twice: KaTeX HTML for the static page (`build/render_math.js`), MathML
via pandoc for the Atom feed.

Why both: KaTeX HTML looks best in browsers but is unusable in RSS readers,
which don't load external CSS. MathML renders natively everywhere but big
operators come out small. Use the best tool for each renderer.

## How to format email recaps

1. Clip image widths to 600 pixels. In Preview, use Tools > Adjust Size
2. In Thunderbird, `Insert > Html ...` then copy the below html
3. Add description and new line for each image
4. Drag each image into Thunderbird and choose "inline image"
5. Highlight all text and images
6. Select `Insert > Html ...` again
7. Add `style="width:100%; max-width:600px; height:auto;"` to each `<img>` tag

```
<!--[if mso]>
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" align="left" style="width:600px;"><tr><td>
<![endif]-->

<table
  role="presentation"
  width="100%"
  cellpadding="0"
  cellspacing="0"
  border="0"
  align="left"
  style="max-width: 600px"
>
  <tr>
    <td
      align="left"
      style="
        padding: 0;
        text-align: left;
        word-break: break-word;
        overflow-wrap: break-word;
      "
    >
      <!-- your content here -->
    </td>
  </tr>
</table>

<!--[if mso]>
</td></tr></table>
<![endif]-->
```

# inspiration

- https://ben.bolte.cc/
- https://gwern.net/index

# Misc

.nojekyll file allows the .well-known/ to be published

# todo

- [ ] remove javascript duplication between templates
- [ ] wrap `<script>` with CDATA at build time for the RSS feed so I don't need
      to specify it for the general posts if i want javascript in them.
- [ ] add a tag to the json if a post is interactive so i can add a warning
      about javascript missing to the RSS posts.
- [ ] figure out why website can't load on some corporate networks/firewalls
