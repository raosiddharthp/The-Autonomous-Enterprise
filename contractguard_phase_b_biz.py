from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Phase B: Business Architecture", show=False, filename="contractguard_phase_b_biz", direction="LR", graph_attr=graph_attr):
    start = Tablet("Contract Signature")
    
    with Cluster("Obligation Lifecycle"):
        onboard = Run("Onboarding & Extraction")
        monitor = Run("Active Compliance Monitoring")
        archive = Run("Renewal / Termination")

    start >> onboard >> monitor >> archive