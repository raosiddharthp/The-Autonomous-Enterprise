from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery, DataCatalog
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk Audit Map", show=False, filename="finrisk_audit_map", direction="LR", graph_attr=graph_attr):
    raw_tx = BigQuery("Raw Transaction\nEvent")

    with Cluster("Governance Trace"):
        logic = BigQuery("Standardization\nLogic")
        audit_trail = DataCatalog("Data Lineage\n(Immutability)")

    reasoning = VertexAI("Agentic Thought\nNode")
    sar_filing = Run("Compliant SAR Filing")

    raw_tx >> Edge(label="Transformed") >> logic
    logic >> Edge(label="Input to Agent") >> reasoning
    reasoning >> Edge(label="Generates", style="bold", color="darkblue") >> sar_filing
    
    [logic, reasoning] - audit_trail