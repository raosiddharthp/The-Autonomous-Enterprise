from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.devtools import GCR
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.analytics import BigQuery

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk MLOps Lifecycle", show=False, filename="finrisk_mlops_lifecycle", direction="LR", graph_attr=graph_attr):
    with Cluster("Continuous Training (CT)"):
        data = BigQuery("Drift/Risk Data")
        trainer = VertexAI("Vertex Training")
        evaluator = VertexAI("Model Validation")

    registry = GCR("Model Registry\n(v2.x.x)")
    deploy = VertexAI("Agent Prediction API")

    data >> trainer >> evaluator >> Edge(label="Approved") >> registry >> deploy