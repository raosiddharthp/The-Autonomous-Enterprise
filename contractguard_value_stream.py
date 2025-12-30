from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Legal Obligation Value Stream", show=False, filename="contractguard_value_stream", direction="LR", graph_attr=graph_attr):
    input_doc = Run("Document Ingestion")
    
    with Cluster("Automated Processing Pipeline"):
        detection = VertexAI("Clause Detection")
        validation = VertexAI("Policy Validation")
        alert = Monitoring("Compliance Alert")

    input_doc >> detection >> validation >> alert