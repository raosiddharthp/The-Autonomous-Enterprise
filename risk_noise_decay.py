from diagrams import Diagram, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram(
    "Outcome: False Positive Decay Curve", 
    show=False, 
    filename="risk_noise_decay", 
    direction="LR", 
    graph_attr=graph_attr
):
    high_noise = Rack("Legacy Heuristics\n(High Noise)")
    bert_triage = VertexAI("BERT-tiny Triage\n(Deployment)")
    low_noise = Rack("Optimized Monitoring\n(90% Noise Reduction)")

    high_noise >> Edge(label="AI Pivot", color="darkred") >> bert_triage >> Edge(label="Precision Gain", color="darkgreen", style="bold") >> low_noise