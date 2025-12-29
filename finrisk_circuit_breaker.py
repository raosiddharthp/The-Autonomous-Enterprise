from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("Financial Circuit Breaker", show=False, filename="finrisk_circuit_breaker", direction="LR", graph_attr=graph_attr):
    drift_monitor = Monitoring("Model Drift\nThreshold")
    
    with Cluster("Agent Runtime"):
        agent = VertexAI("Risk Scoring Agent")
        kill_switch = Run("Circuit Breaker\n(Kill Switch)")

    incident_log = Monitoring("Audit Log\n(Incident Triggered)")

    drift_monitor >> Edge(label="Drift Detected", color="red", style="bold") >> kill_switch
    kill_switch >> Edge(label="Suspend", color="darkred") >> agent
    kill_switch >> Edge(label="Report", color="orange") >> incident_log