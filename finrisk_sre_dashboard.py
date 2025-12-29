from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Looker
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.database import Memorystore

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.5",
    "ranksep": "2.0",
    "bgcolor": "transparent",
    "margin": "0"
}

with Diagram("SRE Golden Signals", show=False, filename="finrisk_sre_dashboard", direction="LR", graph_attr=graph_attr):
    telemetry = Monitoring("GCP Operations\n(Latency/Errors)")
    audit_db = BigQuery("Compliance Data")
    
    with Cluster("Processing Layer"):
        hot_storage = Memorystore("Real-time Stats")
        viz_engine = Looker("SRE Dashboard\n(Golden Signals)")

    telemetry >> Edge(color="darkblue") >> hot_storage
    audit_db >> Edge(color="darkgreen") >> hot_storage
    hot_storage >> Edge(style="bold") >> viz_engine