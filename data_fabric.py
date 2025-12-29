from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import BigQuery, DataCatalog
from diagrams.gcp.security import KeyManagementService, Iam
from diagrams.gcp.compute import Run
from diagrams.gcp.storage import GCS

# Filename: data_fabric.png
with Diagram("BigQuery Data Governance Fabric", show=False, filename="data_fabric", direction="TB"):

    with Cluster("Federated Data Sources (Subsystems)"):
        sources = [
            Run("Contract Guard"),
            Run("RevRec-AI"),
            GCS("GreenOps Logs")
        ]

    with Cluster("Governance & Policy Gates"):
        # We assign the first element to a variable to facilitate the group connection
        iam_gate = Iam("IAM / Policy Tagging")
        gatekeeper = [
            DataCatalog("Data Catalog"),
            iam_gate,
            KeyManagementService("CMEK Encryption")
        ]

    with Cluster("Unified Data Fabric"):
        fabric = BigQuery("BigQuery Omni\n(Federated Queries)")

    # Corrected Flow: Connecting a list to a specific node in the next group
    # Diagrams will automatically draw lines to the cluster
    sources >> Edge(label="Raw Data", style="dashed") >> iam_gate
    gatekeeper >> Edge(label="Governed Access", color="darkblue", style="bold") >> fabric