from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.2", "bgcolor": "transparent"}

with Diagram("Business View: Capability Map", show=False, filename="doc_capability_map", direction="LR", graph_attr=graph_attr):
    with Cluster("Document Intelligence Capabilities"):
        classification = Blank("Document Classification")
        extraction = Blank("Data Extraction\n(Entities)")
        validation = Blank("Quality Validation")
        
    enterprise = Blank("Enterprise\nData Fabric")

    classification >> Edge(label="Feeds") >> enterprise
    extraction >> Edge(label="Feeds") >> enterprise
    validation >> Edge(label="Ensures") >> enterprise