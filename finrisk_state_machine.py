from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk State Machine", show=False, filename="finrisk_state_machine", direction="LR", graph_attr=graph_attr):
    start = Run("Inbound Alert\n(Trigger)")
    
    with Cluster("LangGraph Deterministic Nodes"):
        triage = VertexAI("Triage Node")
        research = VertexAI("Research Node")
        audit = VertexAI("Audit Node")

    archive = Run("Case Archive")

    start >> triage >> Edge(label="High Risk") >> research >> audit >> Edge(label="Log Trail") >> archive
    triage >> Edge(label="False Positive", color="red") >> archive