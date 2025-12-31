from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub, Dataflow, BigQuery
from diagrams.gcp.network import CDN
from diagrams.gcp.security import KeyManagementService

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Phase D: Risk Landing Zone", show=False, filename="risk_event_landing_zone", direction="LR", graph_attr=graph_attr):
    ingress = CDN("External Triggers")
    
    with Cluster("Secure Ingestion Pipeline"):
        bus = Pubsub("Real-Time Risks")
        proc = Dataflow("Security Filter")
        kms = KeyManagementService("KMS Encryption")

    lake = BigQuery("Risk Data Warehouse")

    ingress >> bus >> proc >> lake
    proc >> Edge(label="Encrypt", style="dashed") >> kms