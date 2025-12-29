from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.5", "bgcolor": "transparent"}

with Diagram("FinRisk Value Stream", show=False, filename="finrisk_value_stream", direction="LR", graph_attr=graph_attr):
    ingest = Run("Transaction\nIngestion")
    
    with Cluster("Manual Baseline (Bottleneck)"):
        manual = Run("Manual Investigation\n(48-72 Hours)")

    with Cluster("Agentic Target"):
        ai_agent = VertexAI("Fraud Agent\n(Sub-Minute)")

    filing = Run("Regulatory\nFiling")

    ingest >> Edge(label="Legacy", color="red", style="dashed") >> manual >> filing
    ingest >> Edge(label="Automated", color="darkgreen", style="bold") >> ai_agent >> filing