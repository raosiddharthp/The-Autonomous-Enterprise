from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.compute import Run
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.6", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("MLOps: Lifecycle Handoff", show=False, filename="doc_ml_lifecycle_handoff", direction="LR", graph_attr=graph_attr):
    hf_hub = Blank("Hugging Face Hub\n(Base Model)")
    
    with Cluster("Enterprise Sovereign ML"):
        vertex = VertexAI("Vertex AI\n(Fine-Tuning/Eval)")
        endpoint = Run("Cloud Run\n(Scalable Inference)")
        
    hf_hub >> Edge(label="Import") >> vertex >> Edge(label="Deploy") >> endpoint