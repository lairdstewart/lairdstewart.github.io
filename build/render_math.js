#!/usr/bin/env node
// Reads JSON [{tex, display}, ...] from stdin, writes JSON [html, ...] to stdout.
// Pre-renders TeX to KaTeX HTML for the static site (the Atom feed uses
// pandoc-emitted MathML instead, since RSS readers don't load external CSS).

const katex = require("katex");

let input = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", chunk => { input += chunk; });
process.stdin.on("end", () => {
  const items = JSON.parse(input);
  const out = items.map(item =>
    katex.renderToString(item.tex, {
      displayMode: !!item.display,
      output: "html",
      throwOnError: true,
      strict: "ignore",
    })
  );
  process.stdout.write(JSON.stringify(out));
});
