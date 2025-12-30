from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.gcp.storage import GCS
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Phase D: Technology Architecture", show=False, filename="contractguard_phase_d_tech", direction="LR", graph_attr=graph_attr):
    msa_storage = GCS("Legal Vault\n(MSAs / SOWs)")
    
    with Cluster("Reasoning Engine"):
        gemini = VertexAI("Gemini 1.5 Pro\n(2M Token Context)")
        reasoning = Run("Long-Form Reasoning\nAgent")

    msa_storage >> Edge(label="Large Context Load") >> gemini
    gemini >> reasoning