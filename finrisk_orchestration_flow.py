from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk Orchestration Flow", show=False, filename="finrisk_orchestration_flow", direction="LR", graph_attr=graph_attr):
    supervisor = VertexAI("Compliance Supervisor\n(Orchestrator)")

    with Cluster("Specialist Swarm"):
        researcher = Run("Fraud Researcher")
        auditor = Run("Compliance Auditor")
        filer = Run("SAR Filer")

    supervisor >> Edge(label="Analyze Case", color="darkblue") >> researcher
    researcher >> Edge(label="Case Findings", color="darkgreen", style="dashed") >> supervisor
    supervisor >> Edge(label="Review Findings", color="darkblue") >> auditor
    auditor >> Edge(label="Approved", color="darkgreen", style="dashed") >> supervisor
    supervisor >> Edge(label="Final Filing", color="purple", style="bold") >> filer