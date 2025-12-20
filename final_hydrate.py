import os

projects = {
    "contractguard": {
        "name": "ContractGuard",
        "strategy": "| Legal Ops Managers | Agile CLM Rollout | Accelerated delivery 35% |\n| IT Architects | TOGAF CLM Reference Architecture | Reduced silos 45% |",
        "agents": "AutoGen Swarm for Negotiation Simulation, MemGPT redlining agents",
        "infra": "Document AI, Firestore, VPC Peering for GDPR compliance"
    },
    "revrec-ai": {
        "name": "RevRec-AI: Autonomous Engine",
        "strategy": "| RevOps Leads | Scaled Agile Roadmap | 30% faster deployment |\n| Enterprise Architects | TOGAF ADM Cycle Applied | Reduced compliance risk 40% |",
        "agents": "LangGraph Agent for Multi-Step Reasoning, CrewAI obligation-to-recognition chain",
        "infra": "BigQuery, Cloud Functions, Pub/Sub event-driven setup"
    },
    "strategy-dashboard": {
        "name": "Executive Strategy & Dashboard",
        "strategy": "| CSO | Business Architecture: Strategy Map | 40% increase in alignment |\n| VP Finance | Dashboard Data Security | 100% data confidentiality |",
        "agents": "Strategic Option Synthesis Agent (LangGraph), Executive Summary Model (Mistral)",
        "infra": "BigQuery View Design, Cloud Run Handler, Cloud Monitoring alerts"
    },
    "asset-inventory": {
        "name": "Intelligent Asset Inventory",
        "strategy": "| Solution Train Engineer | Solution Train Readiness | 30% reduced friction |\n| VP Technology | Technology Reference Model (TRM) | 25% technical debt reduction |",
        "agents": "Predictive Maintenance Agent (CrewAI), Field Service Log Summarizer",
        "infra": "IoT Pub/Sub Ingestion, Cloud Run Containerized Deployment"
    },
    "data-governance": {
        "name": "Open Source Data Governance",
        "strategy": "| CDO | Portfolio Vision & Data Governance Epic | 40% increase in trust |\n| Data Architect | Data Architecture View | 30% reduction in complexity |",
        "agents": "Quality Rule Definition Agent (LangChain), Policy Enforcement Model (spaCy)",
        "infra": "GCS Lifecycle Policies, IAM Data Access Policies, Serverless DQ Trigger"
    },
    "risk-monitoring": {
        "name": "Continuous Risk Monitoring",
        "strategy": "| LPM Owner | Lean Budget Guardrails | 35% strategic alignment |\n| CSO | Security Architecture & Compliance View | 50% reduced exposure |",
        "agents": "External Risk Scour Agent (LangGraph), Risk Text Classifier (BERT-tiny)",
        "infra": "VPC Service Controls (VPC-SC), BigQuery ML Anomaly Detection"
    },
    "serverless-ai": {
        "name": "Serverless Document Analyzer",
        "strategy": "| Value Stream Owner | PI Planning Readiness | 25% increased predictability |\n| Chief Architect | Architecture Definition Document | 30% lower TCO |",
        "agents": "Intelligent Document Router Agent, Vertex AI Classification Endpoint",
        "infra": "Cloud Functions, Cloud Storage, Pub/Sub Orchestration"
    }
}

def hydrate():
    base = os.path.expanduser("~/portfolio")
    for slug, data in projects.items():
        doc_path = f"{base}/{slug}/docs"
        os.makedirs(f"{doc_path}/strategy", exist_ok=True)
        os.makedirs(f"{doc_path}/agents", exist_ok=True)
        os.makedirs(f"{doc_path}/infra", exist_ok=True)
        
        with open(f"{doc_path}/strategy/business-case.md", "w") as f:
            f.write(f"# Strategy: {data['name']}\n\n| Persona | Deliverable | Impact |\n| :--- | :--- | :--- |\n{data['strategy']}")
        
        with open(f"{doc_path}/agents/workflow.md", "w") as f:
            f.write(f"# Agentic AI Framework\n\n* {data['agents']}")
            
        with open(f"{doc_path}/infra/stack.md", "w") as f:
            f.write(f"# Cloud Infrastructure (GCP)\n\n* {data['infra']}")

hydrate()
print("✅ Remaining 7 projects successfully hydrated.")
