from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, DataCatalog
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.security import KeyManagementService

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk Data Lineage", show=False, filename="finrisk_lineage", direction="LR", graph_attr=graph_attr):
    raw = BigQuery("Raw Transactions\n(Sensitive)")
    kms = KeyManagementService("CMEK Encryption")
    
    with Cluster("Sovereign Processing"):
        catalog = DataCatalog("Data Lineage\nAudit Trail")
        intel = VertexAI("Risk Inference")

    sar_report = BigQuery("SAR Document\n(Encrypted)")

    raw - kms
    raw >> Edge(label="Traceable", color="darkgreen") >> intel >> sar_report
    intel - catalog