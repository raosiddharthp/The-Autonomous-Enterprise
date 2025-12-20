#!/bin/bash

create_project() {
    local name=$1
    echo "🏗️ Architecting Enterprise Shell: $name"
    
    # 1. Create Comprehensive Folder Hierarchy
    mkdir -p "$name/docs/strategy" \
             "$name/docs/architecture" \
             "$name/docs/agents" \
             "$name/docs/platform" \
             "$name/docs/infra" \
             "$name/docs/governance" \
             "$name/docs/ops" \
             "$name/src/agents" \
             "$name/src/engine" \
             "$name/terraform" \
             "$name/tests"

    # 2. Create the Standardized mkdocs.yml
    cat <<EON > "$name/mkdocs.yml"
site_name: "$name Platform"
theme:
  name: material
  palette:
    primary: google-blue
    accent: light blue
  features:
    - navigation.sections
    - navigation.expand

nav:
  - Overview: index.md
  - 1. Strategy & Discovery:
      - Business Case & Personas: strategy/business-case.md
      - Challenges & Requirements: strategy/requirements.md
  - 2. Architecture Vision:
      - Architecture Artifacts: architecture/artifacts.md
      - Roadmap & Phases: architecture/roadmap.md
  - 3. The Multi-Agent Platform:
      - Agentic Workflow Design: agents/workflow.md
      - Data & ML Architecture: platform/data-ml.md
  - 4. Cloud Infrastructure:
      - Technical Stack: infra/stack.md
      - IaC & CI/CD: infra/automation.md
  - 5. Enterprise Readiness:
      - Governance & Compliance: governance/compliance.md
      - Change Management Plan: governance/change-mgmt.md
  - 6. Operations & Handoff:
      - Support Runbook: ops/handoff.md
      - Observability & SLOs: ops/monitoring.md
EON

    # 3. Initialize blank files so mkdocs serve doesn't error out
    touch "$name/docs/index.md"
    touch "$name/docs/strategy/business-case.md"
    touch "$name/docs/strategy/requirements.md"
    touch "$name/docs/architecture/artifacts.md"
    touch "$name/docs/architecture/roadmap.md"
    touch "$name/docs/agents/workflow.md"
    touch "$name/docs/platform/data-ml.md"
    touch "$name/docs/infra/stack.md"
    touch "$name/docs/infra/automation.md"
    touch "$name/docs/governance/compliance.md"
    touch "$name/docs/governance/change-mgmt.md"
    touch "$name/docs/ops/handoff.md"
    touch "$name/docs/ops/monitoring.md"
}

PROJECTS=("greenops" "finrisk-sentinel" "contractguard" "revrec-ai" "asset-inventory" "risk-monitoring" "data-governance" "strategy-dashboard" "doc-analyzer" "serverless-ai")

for p in "${PROJECTS[@]}"; do
    create_project "$p"
done

echo "✅ All 10 project shells updated to Enterprise Standard."
