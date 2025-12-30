from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.storage import GCS
from diagrams.generic.compute import Rack

graph_attr = {
    "pad": "0.1",
    "nodesep": "1.2",
    "ranksep": "2.0",
    "bgcolor": "transparent"
}

with Diagram(
    "Phase G: RUL Retraining Loop", 
    show=False, 
    filename="asset_retraining_loop", 
    direction="LR", 
    graph_attr=graph_attr
):
    ground_truth = BigQuery("Actual Failure Data")
    
    with Cluster("Vertex AI Pipeline"):
        training = VertexAI("TimesFM Retraining")
        eval = VertexAI("Model Evaluation")
        registry = GCS("Model Registry")

    prod_model = VertexAI("Production Forecaster")

    ground_truth >> training >> eval >> registry >> prod_model
    prod_model >> Edge(label="Inference Drift", style="dashed") >> ground_truth