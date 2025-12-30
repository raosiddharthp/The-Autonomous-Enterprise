from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.device import Tablet

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Outcome: Asset Lifecycle Extension", show=False, filename="asset_lifecycle_extension", direction="LR", graph_attr=graph_attr):
    standard_path = Tablet("Standard Failure Path\n(Legacy)")
    
    with Cluster("AI-Driven Intervention"):
        detector = VertexAI("RUL Detective")
        care = Tablet("Proactive Maintenance")

    extended_life = Tablet("Extended Asset Utility\n(+25% Lifespan)")

    standard_path >> detector >> care >> Edge(label="Deviation", color="blue", style="bold") >> extended_life