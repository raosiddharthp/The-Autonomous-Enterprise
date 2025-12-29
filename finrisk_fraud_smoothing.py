from diagrams import Diagram, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "3.0", "bgcolor": "transparent"}

with Diagram("FinRisk Fraud Smoothing", show=False, filename="finrisk_fraud_smoothing", direction="LR", graph_attr=graph_attr):
    manual_cycle = Run("High-Variance\nManual Detection\n(Spiky Ops)")
    smoothing_agent = VertexAI("Deterministic Agent\n(Continuous/Smooth)")
    outcome = Run("Predictable\nCompliance Posture")

    manual_cycle >> Edge(label="Shift", color="darkred") >> smoothing_agent >> Edge(label="Output", color="darkgreen") >> outcome