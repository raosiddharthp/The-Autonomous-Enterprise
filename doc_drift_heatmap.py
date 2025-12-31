from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("MLE View: Drift Stability", show=False, filename="doc_drift_heatmap", direction="TB", graph_attr=graph_attr):
    with Cluster("Model Performance Zones"):
        high = Rack("95% Accuracy\n(Optimal)")
        mid = Rack("90% Accuracy\n(Drift Detected)")
        low = Rack("Retraining Needed")
    
    loop = VertexAI("Continuous Training\n(CT Pipeline)")
    
    loop >> Edge(label="Corrects", color="darkgreen") >> [high, mid]