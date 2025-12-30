from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.onprem.vcs import Github
from diagrams.gcp.devtools import GCR

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Phase G: Model Registry Lineage", show=False, filename="contractguard_model_registry", direction="LR", graph_attr=graph_attr):
    playbook_commit = Github("Legal Playbook\n(Git Commit)")
    model_version = GCR("Vertex Model Registry\n(v2.4.1)")
    deployment = VertexAI("Production Endpoint")

    playbook_commit >> Edge(label="Retrain Trigger") >> model_version >> deployment