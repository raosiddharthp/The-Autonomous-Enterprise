from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.compute import Run
from diagrams.gcp.security import KeyManagementService
from diagrams.gcp.operations import Monitoring

# Filename: system_context.png
with Diagram("Level 0: Autonomous Enterprise Context", show=False, filename="system_context", direction="LR"):
    
    with Cluster("Central Data Fabric & Event Mesh"):
        mesh = Pubsub("GCP Event Mesh")
        fabric = BigQuery("Data Fabric")

    with Cluster("Core Subsystems"):
        legal = Run("Contract Guard")
        doc_ai = Run("Doc Analyzer")
        rev_rec = Run("RevRec-AI")
        strategy = Monitoring("Strategy Dashboard")

    # Interconnections
    legal >> Edge(label="Events", color="darkblue") >> mesh
    doc_ai >> Edge(label="Metadata", color="darkblue") >> mesh
    mesh >> Edge(label="Orchestration", color="darkblue") >> rev_rec
    
    rev_rec >> Edge(label="Metrics") >> fabric
    fabric >> Edge(label="Insights") >> strategy

    # Global Governance
    governance = KeyManagementService("DQ & Governance")
    governance - Edge(style="dotted") - mesh