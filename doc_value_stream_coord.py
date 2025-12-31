from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Operational View: Value Stream Coordination", show=False, filename="doc_value_stream_coord", direction="LR", graph_attr=graph_attr):
    analyzer = Blank("Document Analyzer\n(Data Source)")
    
    with Cluster("ARTs Consuming Data"):
        revrec = Blank("RevRec-AI ART")
        contract = Blank("ContractGuard ART")
        
    analyzer >> Edge(label="Feeds Structured Data") >> revrec
    analyzer >> Edge(label="Feeds Risk Signals") >> contract