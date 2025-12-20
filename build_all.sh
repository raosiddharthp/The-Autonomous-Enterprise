#!/bin/bash

# 1. Build the Sub-Projects first
PROJECTS=("greenops" "finrisk-sentinel" "contractguard" "revrec-ai" "asset-inventory" "risk-monitoring" "data-governance" "strategy-dashboard" "doc-analyzer" "serverless-ai")

for p in "${PROJECTS[@]}"; do
    if [ -d "$p" ]; then
        echo "Building HTML for: $p"
        cd "$p"
        mkdocs build
        cd ..
    fi
done

# 2. Build the Master Portfolio Hub
echo "Building Master Portfolio Hub..."
mkdocs build

echo "✅ Portfolio Build Complete."
echo "👉 To view, run: mkdocs serve"
