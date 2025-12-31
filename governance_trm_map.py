from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, Pubsub
from diagrams.gcp.compute import Run
from diagrams.gcp.security import Iam
from diagrams.generic.blank import Blank
from diagrams.generic.compute import Rack

# TOGAF Phase C/D: Technology Reference Model
graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "1.5",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase C/D: Governance TRM Map", 
    show=False, 
    filename="governance_trm_map", 
    direction="TB", 
    graph_attr=graph_attr
):
    with Cluster("Open Source Validation Layer"):
        gx_core = Blank("Great Expectations\n(Logic Core)")
        validator = Run("Validation Worker\n(Cloud Run)")

    with Cluster("GCP High-Performance Fabric"):
        warehouse = BigQuery("BigQuery\n(Petabyte Storage)")
        bus = Pubsub("Quality Event Bus")
        
    with Cluster("Governance Perimeter"):
        clac = Iam("Column-Level Access\n(CLAC)")
        audit = Rack("Governance Dashboard\n(Looker)")

    # Data & Logic Flow
    gx_core >> Edge(label="Push Specs") >> validator
    validator >> Edge(label="Execute SQL") >> warehouse
    warehouse >> Edge(label="Metadata Signal") >> bus
    bus >> audit
    clac >> Edge(label="Enforce", style="dashed") >> warehouse