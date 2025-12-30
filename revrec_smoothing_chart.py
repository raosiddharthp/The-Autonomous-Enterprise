from diagrams import Diagram, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.2", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Smoothing Analysis", show=False, filename="revrec_smoothing_chart", direction="LR", graph_attr=graph_attr):
    input_data = Rack("Transaction Stream")
    logic = VertexAI("Smoothing Logic\n(Continuous Recognition)")
    output = Rack("Stable Ledger State")

    input_data >> logic >> output