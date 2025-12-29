from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, DataCatalog
from diagrams.gcp.ml import VertexAI

# Attributes to eliminate white space and force horizontal span
graph_attr = {
    "pad": "0.0",        # Removes inner margins
    "nodesep": "1.5",    # Increases horizontal space between nodes
    "ranksep": "2.0",    # Increases horizontal space between columns
    "bgcolor": "transparent",
    "margin": "0"        # Removes outer canvas margins
}

with Diagram("Information Architecture Lineage", show=False, filename="data_lineage", direction="LR", graph_attr=graph_attr):
    with Cluster("Raw Data Sources"):
        src_billing = VertexAI("GCP Billing API")
        src_carbon = VertexAI("Carbon Footprint API")

    with Cluster("Governance & Storage"):
        storage = BigQuery("Sustainability Lake")
        catalog = DataCatalog("Lineage Tracking")

    report = VertexAI("ESG Reporting Layer")

    src_billing >> Edge(color="darkblue") >> storage
    src_carbon >> Edge(color="darkgreen") >> storage
    storage >> Edge(style="bold") >> report
    storage - catalog