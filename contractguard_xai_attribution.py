from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Governance: XAI Feature Attribution", show=False, filename="contractguard_xai_attribution", direction="LR", graph_attr=graph_attr):
    contract_text = Run("Clause Ingestion\n'Uncapped Liability'")
    
    with Cluster("Vertex Explainable AI"):
        xai_engine = VertexAI("Attribution Engine\n(Integrated Gradients)")
        heatmap = Run("Feature Importance\nHeatmap")

    auditor = Run("Legal Auditor\n(Transparency)")

    contract_text >> xai_engine >> heatmap >> Edge(label="Explain Result") >> auditor