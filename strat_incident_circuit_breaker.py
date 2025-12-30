from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run
from diagrams.generic.compute import Rack

# TOGAF Phase G: Implementation Governance
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase G: Incident Circuit Breaker", 
    show=False, 
    filename="strat_incident_circuit_breaker", 
    direction="LR", 
    graph_attr=graph_attr
):
    monitor = Monitoring("Cloud Monitoring\n(Anomaly Detected)")
    
    with Cluster("Circuit Breaker Pattern"):
        breaker = Rack("Circuit Breaker\n(Isolation)")
        rollback = VertexAI("Prompt Rollback\n(Known Good Ver)")

    swarm = Run("Agent Swarm\n(Cloud Run)")
    
    monitor >> Edge(label="Trigger", color="red", style="bold") >> breaker
    breaker >> Edge(label="Isolate Swarm") >> swarm
    breaker >> Edge(label="Revert State") >> rollback
    rollback >> Edge(label="Restore Service", color="darkgreen") >> swarm