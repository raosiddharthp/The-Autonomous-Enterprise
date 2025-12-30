from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.operations import Monitoring
from diagrams.generic.compute import Rack

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Outcome: Precision-Recall Matrix", show=False, filename="asset_precision_recall", direction="LR", graph_attr=graph_attr):
    with Cluster("Model Evaluation"):
        precision = Monitoring("Precision\n(Avoid False Repairs)")
        recall = Monitoring("Recall\n(Catch All Failures)")
    
    trust_score = Rack("Operational Trust Score\n(99.4%)")

    [precision, recall] >> trust_score