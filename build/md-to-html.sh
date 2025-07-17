#! /bin/sh

SCRIPT_DIR="${0:A:h}"
PARENT_DIR="${SCRIPT_DIR:h}"

for file in "$PARENT_DIR"/markdown/*.md; do
    filename=$(basename "$file" .md)
    pandoc "$file" \
        -s \
        -t html5 \
        --katex \
        --css "$SCRIPT_DIR"/style.css \
        --template "$SCRIPT_DIR"/template.html \
        -o "$PARENT_DIR"/"$filename".html
done
