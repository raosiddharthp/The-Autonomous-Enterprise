from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram(
    "Outcome: Audit Speed Waterfall", 
    show=False, 
    filename="risk_audit_waterfall", 
    direction="LR", 
    graph_attr=graph_attr
):
    legacy_time = Tablet("Legacy Manual Prep\n(100% Time)")
    
    with Cluster("Automated Pipeline"):
        analyzer = Run("Agentic Summarization")
        lineage = Run("Automated Lineage")

    optimized_time = Tablet("Optimized Prep\n(20% Time)")

    legacy_time >> Edge(label="80% Reduction") >> analyzer >> lineage >> optimized_time