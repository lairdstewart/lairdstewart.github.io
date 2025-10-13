#! /bin/zsh

SCRIPT_DIR="${0:A:h}"
PARENT_DIR="${SCRIPT_DIR:h}"
SRC_DIR="$PARENT_DIR/src"
POSTS_DIR="$PARENT_DIR/posts"
RECAPS_DIR="$PARENT_DIR/recaps"

# Create output directories
mkdir -p "$POSTS_DIR"
mkdir -p "$RECAPS_DIR"

# Process index.html (src/index.md -> /index.html)
if [[ -f "$SRC_DIR/index.md" ]]; then
    pandoc "$SRC_DIR/index.md" \
        -s \
        -t html5 \
        --katex \
        --css /build/style.css \
        --template "$SCRIPT_DIR"/template.html \
        -o "$PARENT_DIR/index.html"
fi

# Process posts (src/posts/*.md -> /posts/*.html)
for file in "$SRC_DIR"/posts/*.md; do
    [[ -e "$file" ]] || continue
    filename=$(basename "$file" .md)
    pandoc "$file" \
        -s \
        -t html5 \
        --katex \
        --css /build/style.css \
        --template "$SCRIPT_DIR"/template.html \
        -o "$POSTS_DIR/$filename.html"
done

# Process recaps (src/recaps/*.md -> /recaps/*.html)
for file in "$SRC_DIR"/recaps/*.md; do
    [[ -e "$file" ]] || continue
    filename=$(basename "$file" .md)
    pandoc "$file" \
        -s \
        -t html5 \
        --katex \
        --css /build/style.css \
        --template "$SCRIPT_DIR"/template.html \
        -o "$RECAPS_DIR/$filename.html"
done
