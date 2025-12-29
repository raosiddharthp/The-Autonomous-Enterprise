from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.network import VPC, Armor
from diagrams.gcp.security import KeyManagementService, Iam
from diagrams.gcp.storage import GCS
from diagrams.gcp.compute import GKE
from diagrams.gcp.analytics import BigQuery

# Filename: landing_zone.png
with Diagram("Sovereign Landing Zone Architecture", show=False, filename="landing_zone", direction="TB"):

    iam = Iam("Identity & Access Management")
    
    with Cluster("VPC Service Control Perimeter"):
        armor = Armor("Cloud Armor (WAF)")
        
        with Cluster("Regulated Data Region (EU/US)"):
            keys = KeyManagementService("CMEK (Encryption)")
            
            with Cluster("Compute Layer"):
                apps = GKE("Hardened GKE Clusters")
            
            with Cluster("Data Layer"):
                storage = GCS("Sovereign Buckets")
                db = BigQuery("Encrypted Data Fabric")

    # Security Flows
    iam >> Edge(label="RBAC", style="dotted") >> apps
    keys >> Edge(label="Envelope Encryption", color="darkblue") >> [storage, db]
    armor >> Edge(label="DDoS Protection") >> apps
    apps >> Edge(label="Private Access") >> db