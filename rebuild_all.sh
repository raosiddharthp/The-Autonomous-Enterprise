#!/bin/bash

PROJECTS=("greenops" "finrisk-sentinel" "contractguard" "revrec-ai" "asset-inventory" "risk-monitoring" "data-governance" "strategy-dashboard" "doc-analyzer" "serverless-ai")

for p in "${PROJECTS[@]}"; do
    echo "🏗️  Building Universal Structure for: $p"
    
    # 1. Create Folder Hierarchy
    mkdir -p "$p/docs/strategy" "$p/docs/architecture" "$p/docs/agents" \
             "$p/docs/platform" "$p/docs/infra" "$p/docs/governance" "$p/docs/ops"

    # 2. Create the "Home" file for the ribbon tab (Fixes the 404)
    echo "# $p Platform Overview" > "$p/docs/index.md"
    echo "This is the technical entry point for the $p project." >> "$p/docs/index.md"

    # 3. Create all sub-pages for the sidebar
    touch "$p/docs/strategy/business-case.md"
    touch "$p/docs/strategy/requirements.md"
    touch "$p/docs/architecture/artifacts.md"
    touch "$p/docs/architecture/roadmap.md"
    touch "$p/docs/agents/workflow.md"
    touch "$p/docs/platform/data-ml.md"
    touch "$p/docs/infra/stack.md"
    touch "$p/docs/infra/automation.md"
    touch "$p/docs/governance/compliance.md"
    touch "$p/docs/governance/change-mgmt.md"
    touch "$p/docs/ops/handoff.md"
    touch "$p/docs/ops/monitoring.md"
    
    # Add temporary headers to all so they aren't empty
    find "$p/docs" -name "*.md" -exec sh -c 'echo "# $(basename {})" > "{}"' \;
done

echo "✅ All project shells are physically present."
