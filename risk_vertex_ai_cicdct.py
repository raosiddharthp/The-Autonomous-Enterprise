from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.devtools import Build, GCR
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Phase G: Vertex AI CI/CD/CT", show=False, filename="risk_vertex_ai_cicdct", direction="LR", graph_attr=graph_attr):
    investigator_labels = Rack("Risk Investigator\n(New Labels)")
    with Cluster("Continuous Training Pipeline"):
        data = BigQuery("Training Data\n(ARIMA & K-Means)")
        build = Build("Cloud Build (CI/CD)")
        container = GCR("Container Registry")
        train = VertexAI("Managed Training")
        endpoint = VertexAI("Online Endpoint")
    investigator_labels >> data >> build >> container >> train >> endpoint