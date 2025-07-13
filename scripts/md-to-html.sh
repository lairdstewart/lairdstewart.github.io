#!/bin/bash
# Converts a Markdown file to HTML using Pandoc with KaTeX, custom CSS, and a template.
# Outputs HTML to the parent directory of the script. Usage: markdown_to_html <input_file.md>

HTML_TEMPLATE_PATH="~/lairdstewart.github.io/build/template.html"
CSS_URL="https://lairdstewart.com/style.css"

INPUT_FILE="$1"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
OUTPUT_DIR="${SCRIPT_DIR}/../"
FILENAME_NO_EXT=$(basename "${INPUT_FILE}" .md)
OUTPUT_FILE="${OUTPUT_DIR}/${FILENAME_NO_EXT}.html"
RESOLVED_HTML_TEMPLATE_PATH=$(eval echo "${HTML_TEMPLATE_PATH}")

pandoc "${INPUT_FILE}" \
       -s \
       -t html5 \
       --katex \
       --css "${CSS_URL}" \
       --template "${RESOLVED_HTML_TEMPLATE_PATH}" \
       -o "${OUTPUT_FILE}"
