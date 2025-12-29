from diagrams import Diagram, Edge
from diagrams.custom import Custom
from diagrams.gcp.ml import VertexAI

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("FinRisk Theme Alignment", show=False, filename="finrisk_theme_alignment", direction="LR", graph_attr=graph_attr):
    theme = VertexAI("Strategic Theme:\nReduce Compliance OpEx")
    hypothesis = VertexAI("Epic Hypothesis:\nAgentic SAR Generation")
    outcome = VertexAI("Key Result:\n90% Reduction in\nManual Investigation")

    theme >> Edge(label="Informs", color="darkblue") >> hypothesis >> Edge(label="Delivers", color="darkblue") >> outcome