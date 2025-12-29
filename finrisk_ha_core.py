from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub, Dataflow
from diagrams.gcp.network import LoadBalancing

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk HA Core", show=False, filename="finrisk_ha_core", direction="LR", graph_attr=graph_attr):
    lb = LoadBalancing("Global LB")

    with Cluster("Region: us-central1 (Multi-Zone)"):
        with Cluster("Zone A"):
            ps_a = Pubsub("Pub/Sub Topic")
            df_a = Dataflow("Dataflow Job")
        
        with Cluster("Zone B"):
            ps_b = Pubsub("Pub/Sub Topic")
            df_b = Dataflow("Dataflow Job")

    lb >> Edge(color="darkblue") >> [ps_a, ps_b]
    ps_a >> df_a
    ps_b >> df_b