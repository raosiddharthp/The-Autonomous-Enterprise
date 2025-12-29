from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import VPC, LoadBalancing
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import VertexAI

# Robust imports for Security components
try:
    from diagrams.gcp.security import Iap as IAP, Armor as CloudArmor
except ImportError:
    try:
        from diagrams.gcp.security import IdentityAwareProxy as IAP, CloudArmor
    except ImportError:
        from diagrams.gcp.security import SecurityScanner as IAP, SecurityScanner as CloudArmor

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk Zero Trust", show=False, filename="finrisk_zero_trust", direction="LR", graph_attr=graph_attr):
    waf = CloudArmor("Cloud Armor\n(WAF/DDoS)")
    lb = LoadBalancing("Global HTTP(S) LB")

    with Cluster("VPC Service Perimeter"):
        net = VPC("Restricted Data VPC")
        risk_data = BigQuery("Sensitive Risk Lake")
        inference = VertexAI("Risk Inference Engine")

    lb >> Edge(label="Filtered") >> waf >> net >> [risk_data, inference]