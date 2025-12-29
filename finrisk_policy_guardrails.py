from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.security import SecretManager
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk Policy Guardrails", show=False, filename="finrisk_policy_guardrails", direction="LR", graph_attr=graph_attr):
    admin = Run("Compliance Admin\n(GitOps)")
    
    with Cluster("Governance Tier"):
        vault = SecretManager("Secret Manager\n(YAML Policies)")
        audit = Run("Cloud Audit Logs")

    agents = VertexAI("Risk Agent Swarm")

    admin >> Edge(label="Push Policy", color="darkblue") >> vault
    vault >> Edge(label="Real-time Pull", color="darkgreen", style="bold") >> agents
    vault - audit