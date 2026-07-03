## Usage

New posts: drop `<slug>.html` + `<slug>.json` (`title`, `date`) into
`src/content/blog/` or `src/content/newsletter/`. The HTML body must be valid
XHTML.

Build: `python3 build/build.py`. Requires `pandoc` and `node` on PATH;
`npm install` once.

Run: ./build/server.sh

Start OCI remark42 instance:

- `ssh -i keys/oracle-compute-instance/ssh-key-2026-06-14.key opc@157.151.137.162`

## Math

Posts use `<span class="math inline|display">TEX</span>`. Each expression is
rendered twice: KaTeX HTML for the static page (`build/render_math.js`), MathML
via pandoc for the Atom feed.

Why both: KaTeX HTML looks best in browsers but is unusable in RSS readers,
which don't load external CSS. MathML renders natively everywhere but big
operators come out small. Use the best tool for each renderer.

## Email recaps

Clip image widths to 600 pixels. In Preview, use Tools > Adjust Size. In Place
html in the following table. In Thunderbird, first add photos, then insert the
html above it with Insert > Html ...

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
