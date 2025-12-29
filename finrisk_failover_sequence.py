from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.5", "bgcolor": "transparent"}

with Diagram("FinRisk Failover Sequence", show=False, filename="finrisk_failover_sequence", direction="LR", graph_attr=graph_attr):
    lb = LoadBalancing("Traffic Manager")
    health = Monitoring("Health Check\n(Primary Down)")

    with Cluster("Primary Region (us-east1)"):
        primary = Run("Primary Workers\n(Degraded)")

    with Cluster("Failover Region (us-west1)"):
        secondary = Run("Secondary Workers\n(Active)")

    health >> Edge(label="Failover Trigger", color="darkred", style="dashed") >> lb
    lb >> Edge(label="Reroute (sub-ms)", color="darkgreen", style="bold") >> secondary
    lb >> Edge(label="Drain", color="gray") >> primary