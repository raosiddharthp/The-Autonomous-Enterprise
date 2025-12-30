from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Strategic Playbook: Contract Integration", show=False, filename="contractguard_strategic_playbook", direction="LR", graph_attr=graph_attr):
    contract_agent = VertexAI("ContractGuard Agent\n(Extraction)")
    valid_data = BigQuery("Pre-Validated\nLegal Metadata")
    revrec_agent = VertexAI("RevRec-AI Agent\n(Recognition)")
    
    contract_agent >> Edge(label="Validate Clauses", color="darkgreen", style="bold") >> valid_data >> Edge(label="Input", color="darkblue") >> revrec_agent