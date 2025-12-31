from diagrams import Diagram, Edge
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("SAFe View: Speed Waterfall", show=False, filename="doc_speed_waterfall", direction="LR", graph_attr=graph_attr):
    manual = Blank("Manual Triage\n(48 Hours)")
    automated = Blank("AI Extraction\n(30 Seconds)")
    value = Blank("Structured Action\n(Sub-Second)")

    manual >> Edge(label="Eliminate Waste", color="darkred") >> automated >> Edge(color="darkgreen", style="bold") >> value