from diagrams import Diagram, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("XAI: Feature Attribution Map", show=False, filename="doc_xai_heatmap", direction="TB", graph_attr=graph_attr):
    doc_input = Blank("Raw PDF/OCR\nTokens")
    attribution = VertexAI("Explainable AI\n(Integrated Gradients)")
    heatmap = Blank("Spatial Heatmap\n(Field Importance)")

    doc_input >> Edge(label="Analyze") >> attribution >> heatmap