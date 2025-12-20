import os

# This dictionary stores the "Enterprise Intelligence" for your projects
projects = {
    "greenops": {
        "name": "GreenOps Platform",
        "strategy_rows": "| Sustainability Manager | Agile Roadmap | 25% quicker initiatives |\n| CIO | TOGAF Sustainability Framework | Aligned IT with ESG |",
        "agents": "LangChain Agent for Workload Shifting, Gemini auto-adjustments",
        "infra": "Terraform for Multi-region GKE, Billing APIs, Python/Pandas migration logic"
    },
    "finrisk-sentinel": {
        "name": "FinRisk Sentinel",
        "strategy_rows": "| Compliance Teams | SAFe Anti-Fraud Deployment | Reduced rollout time 40% |\n| Security Architects | TOGAF FinCrime Architecture | Enhanced security 50% |",
        "agents": "CrewAI Swarm for Multi-Agent Compliance, LangGraph screening logic",
        "infra": "GCP Pub/Sub, Memorystore, GKE for agent hosting"
    },
    "contractguard": {
        "name": "ContractGuard",
        "strategy_rows": "| Legal Ops Managers | Agile CLM Rollout | Accelerated delivery 35% |\n| IT Architects | TOGAF CLM Reference Architecture | Reduced silos 45% |",
        "agents": "AutoGen Swarm for Negotiation Simulation, MemGPT redlining agents",
        "infra": "Document AI, Firestore, VPC Peering for GDPR compliance"
    }
    # (Note: You can add the other 7 projects here following the same keys)
}

def hydrate_portfolio():
    for slug, data in projects.items():
        base_docs = os.path.expanduser(f"~/portfolio/{slug}/docs")
        
        # Create necessary directories
        os.makedirs(f"{base_docs}/strategy", exist_ok=True)
        os.makedirs(f"{base_docs}/architecture", exist_ok=True)
        os.makedirs(f"{base_docs}/agents", exist_ok=True)
        os.makedirs(f"{base_docs}/infra", exist_ok=True)

        # Populate Strategy Page
        with open(f"{base_docs}/strategy/business-case.md", "w") as f:
            f.write(f"# Strategy: {data['name']}\n\n### Persona Mapping\n| Persona | Deliverable | Impact |\n| :--- | :--- | :--- |\n{data['strategy_rows']}")

        # Populate Agents Page
        with open(f"{base_docs}/agents/workflow.md", "w") as f:
            f.write(f"# Agentic AI Framework\n\n### Intelligence Layer\n* {data['agents']}")

        # Populate Infra Page
        with open(f"{base_docs}/infra/stack.md", "w") as f:
            f.write(f"# Technical Stack (GCP)\n\n### Cloud Architecture\n* {data['infra']}")

    print("🚀 All project documentation sites have been hydrated.")

if __name__ == "__main__":
    hydrate_portfolio()