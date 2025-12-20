#!/bin/bash

# Define the projects array
PROJECTS=("greenops" "finrisk-sentinel" "contractguard" "revrec-ai" "asset-inventory" "risk-monitoring" "data-governance" "strategy-dashboard" "doc-analyzer" "serverless-ai")

# 1. Function to create the structure and initial content
create_project_structure() {
    local p=$1
    echo "🏗️  Building Enterprise Shell for: $p"
    
    # Create the folder hierarchy
    mkdir -p "$p/docs/strategy" "$p/docs/architecture" "$p/docs/agents" \
             "$p/docs/platform" "$p/docs/infra" "$p/docs/governance" "$p/docs/ops"

    # Create placeholder files to prevent 404s
    FILES=(
        "docs/index.md" "docs/strategy/business-case.md" "docs/strategy/requirements.md"
        "docs/architecture/artifacts.md" "docs/architecture/roadmap.md"
        "docs/agents/workflow.md" "docs/platform/data-ml.md"
        "docs/infra/stack.md" "docs/infra/automation.md"
        "docs/governance/compliance.md" "docs/governance/change-mgmt.md"
        "docs/ops/handoff.md" "docs/ops/monitoring.md"
    )
    
    for file in "${FILES[@]}"; do
        echo "# $p - ${file##*/}" > "$p/$file"
    done
}

# 2. Run the loop
for p in "${PROJECTS[@]}"; do
    create_project_structure "$p"
done

# 3. Inject the Master mkdocs.yml to connect everything
cat <<EON > mkdocs.yml
site_name: "Technical Architecture Portfolio"
theme:
  name: material
  palette:
    primary: indigo
    accent: blue
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand

nav:
  - Home: index.md
$(for p in "${PROJECTS[@]}"; do
echo "  - ${p^^}:"
echo "      - Overview: $p/docs/index.md"
echo "      - 1. Strategy & Discovery:"
echo "          - Business Case: $p/docs/strategy/business-case.md"
echo "          - Requirements: $p/docs/strategy/requirements.md"
echo "      - 2. Architecture Vision:"
echo "          - Artifacts: $p/docs/architecture/artifacts.md"
echo "          - Roadmap: $p/docs/architecture/roadmap.md"
echo "      - 3. Multi-Agent Platform:"
echo "          - Workflow Design: $p/docs/agents/workflow.md"
echo "          - Data & ML: $p/docs/platform/data-ml.md"
echo "      - 4. Cloud Infrastructure:"
echo "          - Technical Stack: $p/docs/infra/stack.md"
echo "          - Automation: $p/docs/infra/automation.md"
echo "      - 5. Enterprise Readiness:"
echo "          - Compliance: $p/docs/governance/compliance.md"
echo "          - Change Mgmt: $p/docs/governance/change-mgmt.md"
echo "      - 6. Operations & Handoff:"
echo "          - Support: $p/docs/ops/handoff.md"
echo "          - Monitoring: $p/docs/ops/monitoring.md"
done)
EON

echo "✅ All 10 project shells built and mapped to navigation."
