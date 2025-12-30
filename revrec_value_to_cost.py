from diagrams import Diagram, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.operations import Monitoring

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("RevRec Value-to-Cost", show=False, filename="revrec_value_to_cost", direction="LR", graph_attr=graph_attr):
    labor_cost = Run("Legacy Ops Cost\n($M Manual Labor)")
    serverless_cost = Monitoring("Serverless FinOps\n($K Infrastructure)")
    roai = Run("90% Efficiency\nRealization")

    labor_cost >> Edge(label="Mitigate", color="darkred") >> serverless_cost >> Edge(label="ROI", color="darkgreen", style="bold") >> roai