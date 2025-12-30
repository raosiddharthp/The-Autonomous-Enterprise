from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.ml import VertexAI
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RUL Drift & HITL Feedback", show=False, filename="asset_rul_drift_trend", direction="LR", graph_attr=graph_attr):
    live_preds = VertexAI("RUL Inference")
    drift_monitor = Monitoring("Maintenance Drift\nTrend")
    
    with Cluster("Human-in-the-Loop"):
        technician = Tablet("Technician Review")
        thumbs_up = Monitoring("Accuracy Reinforcement")

    live_preds >> drift_monitor
    drift_monitor >> Edge(label="Trigger Review", color="red") >> technician
    technician >> Edge(label="Thumbs Up", color="darkgreen", style="bold") >> thumbs_up >> Edge(label="Retrain", color="purple") >> live_preds