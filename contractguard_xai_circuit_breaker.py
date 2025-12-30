from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Resilience: MLOps Circuit Breaker", show=False, filename="contractguard_xai_circuit_breaker", direction="LR", graph_attr=graph_attr):
    live_model = VertexAI("Challenger Model\n(Active)")
    champion = VertexAI("Champion Model\n(Fallback)")
    monitor = Monitoring("ROUGE/Drift Monitor")

    monitor >> Edge(label="Accuracy Decay < 90%", color="red", style="bold") >> live_model
    live_model >> Edge(label="Automated Rollback", color="darkgreen") >> champion