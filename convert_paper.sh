#!/usr/bin/env bash
# Convert a PDF paper to markdown using marker-pdf.
#
# Prerequisites:
#   uv tool install marker-pdf
#
# Usage:
#   ./convert_paper.sh path/to/paper.pdf
#   ./convert_paper.sh path/to/paper.pdf --use_llm   # Use LLM for better quality
#
# The converted output lands in incoming_papers/, ready for organize_papers.py.
# LLM mode reads ANTHROPIC_API_KEY from .env (or environment).

set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <pdf_path> [--use_llm]"
    exit 1
fi

PDF_PATH="$1"
shift

if [ ! -f "$PDF_PATH" ]; then
    echo "Error: File not found: $PDF_PATH"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/incoming_papers"
mkdir -p "$OUTPUT_DIR"

# Load .env if it exists (for API keys)
if [ -f "$SCRIPT_DIR/.env" ]; then
    set -a
    source "$SCRIPT_DIR/.env"
    set +a
fi

USE_LLM=false
for arg in "$@"; do
    if [ "$arg" = "--use_llm" ]; then
        USE_LLM=true
    fi
done

if [ "$USE_LLM" = true ]; then
    if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
        echo "Error: ANTHROPIC_API_KEY not set. Add it to .env or export it."
        exit 1
    fi
    echo "Converting $PDF_PATH with LLM assistance (Claude)..."
    TORCH_DEVICE=cpu marker_single "$PDF_PATH" \
        --use_llm \
        --llm_service marker.services.claude.ClaudeService \
        --claude_api_key "$ANTHROPIC_API_KEY" \
        --output_dir "$OUTPUT_DIR"
else
    echo "Converting $PDF_PATH (no LLM)..."
    TORCH_DEVICE=cpu marker_single "$PDF_PATH" \
        --output_dir "$OUTPUT_DIR"
fi

echo ""
echo "Done. Now run: uv run organize_papers.py"
