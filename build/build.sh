#! /bin/zsh

SCRIPT_DIR="${0:A:h}"
PARENT_DIR="${SCRIPT_DIR:h}"
SRC_DIR="$PARENT_DIR/src"
POSTS_DIR="$PARENT_DIR/posts"
ROUNDUPS_DIR="$PARENT_DIR/roundups"

# Process index.html (src/index.md -> /index.html)
pandoc "$SRC_DIR/index.md" \
    -s \
    -t html5 \
    --katex \
    --css /build/style.css \
    --template "$SCRIPT_DIR"/template.html \
    -o "$PARENT_DIR/index.html"

# Process posts (src/posts/*.md -> /posts/*.html)
for file in "$SRC_DIR"/posts/*.md; do
    filename=$(basename "$file" .md)
    pandoc "$file" \
        -s \
        -t html5 \
        --katex \
        --css /build/style.css \
        --template "$SCRIPT_DIR"/template.html \
        -o "$POSTS_DIR/$filename.html"
done

# Process roundups (src/roundups/*.md -> /roundups/*.html)
for file in "$SRC_DIR"/roundups/*.md; do
    filename=$(basename "$file" .md)
    pandoc "$file" \
        -s \
        -t html5 \
        --katex \
        --css /build/style.css \
        --template "$SCRIPT_DIR"/template.html \
        -o "$ROUNDUPS_DIR/$filename.html"
done
