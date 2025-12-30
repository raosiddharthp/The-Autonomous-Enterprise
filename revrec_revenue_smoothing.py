from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Revenue Smoothing", show=False, filename="revrec_revenue_smoothing", direction="LR", graph_attr=graph_attr):
    with Cluster("Manual Cycle"):
        spiky = Run("Manual Entry\n(High Variance)")
    
    with Cluster("AI-Native Core"):
        smooth = VertexAI("RevRec-AI\n(Deterministic Line)")

    outcome = Run("Financial Reporting\nStability")

    spiky >> Edge(label="Replace Spikes", color="red") >> outcome
    smooth >> Edge(label="Integrated Flow", color="darkgreen", style="bold") >> outcome