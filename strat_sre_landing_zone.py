from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import LoadBalancing, CDN
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring
from diagrams.gcp.devtools import Terraform

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Phase D: SRE Landing Zone", show=False, filename="strat_sre_landing_zone", direction="TB", graph_attr=graph_attr):
    with Cluster("IaC Foundation"):
        tf = Terraform("Project Factory")
    lb = LoadBalancing("Global HTTP(S) LB")
    cdn = CDN("Cloud CDN")
    with Cluster("Region: us-central1 (Active)"):
        primary_app = Run("Executive Hub API")
    with Cluster("Region: us-east4 (Failover)"):
        secondary_app = Run("Executive Hub API")
    with Cluster("SRE Control Plane"):
        trace = Monitoring("Cloud Trace\n(Insight Journey)")
        finops = Monitoring("FinOps Dashboard\n(Cost-per-Insight)")
    tf >> Edge(label="Deploy") >> [primary_app, secondary_app]
    lb >> cdn >> [primary_app, secondary_app]
    [primary_app, secondary_app] >> trace
    [primary_app, secondary_app] >> finops