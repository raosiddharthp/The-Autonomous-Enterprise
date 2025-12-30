from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import Pubsub
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("SAFe Solution: Portfolio Sync", show=False, filename="contractguard_portfolio_sync", direction="LR", graph_attr=graph_attr):
    cg = VertexAI("ContractGuard\n(Legal Agent)")
    bus = Pubsub("Cloud Pub/Sub\n(Enterprise Bus)")
    rr = VertexAI("RevRec-AI\n(Financial Agent)")
    
    ledger = Rack("General Ledger\n(Revenue Adjustment)")

    cg >> Edge(label="Indemnity Change", color="darkred") >> bus
    bus >> Edge(label="Trigger Audit", color="darkblue") >> rr >> ledger