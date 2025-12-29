from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk Value Stream Realization", show=False, filename="finrisk_value_stream_realization", direction="LR", graph_attr=graph_attr):
    start = Run("Fraud Trigger")
    
    with Cluster("Legacy (Manual Bottlenecks)"):
        manual_rev = Run("Manual Review\n(Weeks)")
        legacy_filing = Run("Batch Filing")

    with Cluster("Sentinel (Agentic Path)"):
        agent_audit = VertexAI("Compliance Agent\n(Minutes)")
        auto_filing = Run("API Filing")

    start >> Edge(label="Manual Path", color="red", style="dashed") >> manual_rev >> legacy_filing
    start >> Edge(label="Agentic Path", color="darkgreen", style="bold") >> agent_audit >> auto_filing