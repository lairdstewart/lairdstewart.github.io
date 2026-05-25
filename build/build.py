#!/usr/bin/env python3
"""Build rendered HTML pages and Atom feed from src/content/ fragments."""

import html
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
CONTENT = SRC / "content"
BUILD = ROOT / "build"

MATH_SPAN = re.compile(
    r'<span\s+class="math\s+(inline|display)"[^>]*>(.*?)</span>',
    re.DOTALL,
)
MATHML_ELEMENT = re.compile(r'<math\b[^>]*>.*?</math>', re.DOTALL)


def fail(msg):
    sys.stderr.write(f"build: {msg}\n")
    sys.exit(1)


def validate_xhtml(path):
    body = path.read_text()
    wrapped = f'<div xmlns="http://www.w3.org/1999/xhtml">\n{body}\n</div>'
    result = subprocess.run(
        ["xmllint", "--noout", "-"],
        input=wrapped,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail(f"invalid XHTML in {path}:\n{result.stderr}")


def load_sidecar(html_path):
    json_path = html_path.with_suffix(".json")
    if not json_path.exists():
        fail(f"missing sidecar: {json_path}")
    data = json.loads(json_path.read_text())
    for key in ("title", "date"):
        if key not in data:
            fail(f"{json_path}: missing '{key}'")
    try:
        datetime.strptime(data["date"], "%Y-%m-%d")
    except ValueError:
        fail(f"{json_path}: invalid date '{data['date']}', expected YYYY-MM-DD")
    return data


def format_display_date(iso):
    dt = datetime.strptime(iso, "%Y-%m-%d")
    return f"{dt.month}/{dt.day}/{dt.year % 100}"


def render(template, mapping):
    out = template
    for key, val in mapping.items():
        out = out.replace("{{" + key + "}}", val)
    return out


def _collect_math(bodies):
    items = []
    for body in bodies:
        for m in MATH_SPAN.finditer(body):
            items.append((m.group(1) == "display", html.unescape(m.group(2)).strip()))
    return items


def _substitute(bodies, rendered):
    it = iter(rendered)
    return [MATH_SPAN.sub(lambda _: next(it), body) for body in bodies]


def render_math_katex(bodies):
    """Substitute math spans with pre-rendered KaTeX HTML (for the static page)."""
    items = _collect_math(bodies)
    if not items:
        return bodies
    payload = [{"tex": tex, "display": display} for display, tex in items]
    result = subprocess.run(
        ["node", str(BUILD / "render_math.js")],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail(f"katex render failed:\n{result.stderr}")
    return _substitute(bodies, json.loads(result.stdout))


def render_math_pandoc(bodies):
    """Substitute math spans with MathML via pandoc (for the Atom feed)."""
    items = _collect_math(bodies)
    if not items:
        return bodies
    latex_doc = "\n\n".join(
        (f"\\[{tex}\\]" if display else f"\\({tex}\\)") for display, tex in items
    )
    result = subprocess.run(
        ["pandoc", "-f", "latex", "-t", "html", "--mathml"],
        input=latex_doc,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail(f"pandoc render failed:\n{result.stderr}")
    rendered = MATHML_ELEMENT.findall(result.stdout)
    if len(rendered) != len(items):
        fail(f"pandoc returned {len(rendered)} <math> elements, expected {len(items)}")
    return _substitute(bodies, rendered)


def main():
    blog_template = (SRC / "blog.template.html").read_text()
    newsletter_template = (SRC / "newsletter.template.html").read_text()
    page_template = (SRC / "page.template.html").read_text()
    feed_template = (SRC / "feed.template.xml").read_text()

    blog_dir = CONTENT / "blog"
    news_dir = CONTENT / "newsletter"

    # 1. Validate every body fragment.
    fragments = []
    fragments += sorted(blog_dir.glob("*.html"))
    fragments += sorted(news_dir.glob("*.html"))
    fragments += [CONTENT / "index.html", CONTENT / "rss.html"]
    for path in fragments:
        validate_xhtml(path)

    # 2. Render blog entries.
    blog_paths = sorted(blog_dir.glob("*.html"))
    src_bodies = [p.read_text().rstrip() for p in blog_paths]
    page_bodies = render_math_katex(src_bodies)
    feed_bodies = render_math_pandoc(src_bodies)
    blog_entries = []
    for src_path, page_body, feed_body in zip(blog_paths, page_bodies, feed_bodies):
        meta = load_sidecar(src_path)
        slug = src_path.stem
        page = render(blog_template, {
            "TITLE": meta["title"],
            "DATE_DISPLAY": format_display_date(meta["date"]),
            "BODY": page_body,
        })
        out = ROOT / "blog" / f"{slug}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page)
        blog_entries.append({"kind": "blog", "slug": slug, "title": meta["title"], "date": meta["date"], "body": feed_body})

    # 3. Render newsletter entries.
    news_paths = sorted(news_dir.glob("*.html"))
    src_bodies = [p.read_text().rstrip() for p in news_paths]
    page_bodies = render_math_katex(src_bodies)
    feed_bodies = render_math_pandoc(src_bodies)
    news_entries = []
    for src_path, page_body, feed_body in zip(news_paths, page_bodies, feed_bodies):
        meta = load_sidecar(src_path)
        slug = src_path.stem
        page = render(newsletter_template, {
            "TITLE": meta["title"],
            "BODY": page_body,
        })
        out = ROOT / "newsletter" / f"{slug}.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page)
        news_entries.append({"kind": "newsletter", "slug": slug, "title": meta["title"], "date": meta["date"], "body": feed_body})

    # 4. Render top-level pages.
    for name in ("index.html", "rss.html"):
        body = (CONTENT / name).read_text().rstrip()
        page = render(page_template, {"BODY": body})
        (ROOT / name).write_text(page)

    # 5. Render feed.
    all_entries = sorted(blog_entries + news_entries, key=lambda e: e["date"], reverse=True)
    entry_xml = []
    for e in all_entries:
        path = f"{e['kind']}/{e['slug']}.html" if e["kind"] == "blog" else f"newsletter/{e['slug']}.html"
        entry_xml.append(
            f"  <entry>\n"
            f"    <id>https://www.lairdstewart.com/{path}</id>\n"
            f"    <title>{e['title']}</title>\n"
            f"    <updated>{e['date']}T00:00:00Z</updated>\n"
            f"    <link rel=\"alternate\" href=\"{path}\"/>\n"
            f"    <content type=\"xhtml\">\n"
            f"      <div xmlns=\"http://www.w3.org/1999/xhtml\">\n"
            f"{e['body']}\n"
            f"      </div>\n"
            f"    </content>\n"
            f"  </entry>"
        )
    feed_updated = (all_entries[0]["date"] if all_entries else datetime.now().strftime("%Y-%m-%d")) + "T00:00:00Z"
    feed = render(feed_template, {
        "ENTRIES": "\n".join(entry_xml),
        "FEED_UPDATED": feed_updated,
    })
    (ROOT / "feed").write_text(feed)

    print(f"built {len(blog_entries)} blog, {len(news_entries)} newsletter entries")


if __name__ == "__main__":
    main()
