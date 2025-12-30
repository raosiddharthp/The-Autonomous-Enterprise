from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.storage import GCS
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import NaturalLanguageAPI
from diagrams.gcp.network import VirtualPrivateCloud
from diagrams.gcp.security import Iam

# TOGAF Phase D: Technology Architecture - Data Sovereignty Perimeter
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "VPC-SC Governance Perimeter: Multi-Service Boundary",
    show=False,
    filename="contractguard_vpcs_perimeter",
    direction="TB", # Vertical flow to show the boundary 'wrapping' the services
    graph_attr=graph_attr
):
    iam = Iam("Access Context\nManager")

    with Cluster("VPC Service Perimeter (Restricted Region)"):
        # The 'Heart' of the legal data fabric
        vault = GCS("Legal Vault\n(Sensitive PDFs)")
        analysis = NaturalLanguageAPI("Vertex AI\n(Clause Extraction)")
        results = BigQuery("Risk Analytics\n(BQ Dataset)")
        
        perimeter_line = VirtualPrivateCloud("Service Control Boundary")

    # Access is only granted via Bridge or Context
    iam >> Edge(label="Validate Context", color="darkgreen", style="bold") >> perimeter_line
    perimeter_line >> [vault, analysis, results]

    # Outside the perimeter (Access Denied by default)
    internet = Iam("External / Public\n(Access Denied)")
    internet >> Edge(label="Exfiltration Blocked", color="red", style="dotted") >> perimeter_line