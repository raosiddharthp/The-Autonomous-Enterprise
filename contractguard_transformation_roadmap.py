from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.5", "ranksep": "2.0", "bgcolor": "transparent"}

with Diagram("Legal-Tech Transformation Roadmap", show=False, filename="contractguard_transformation_roadmap", direction="LR", graph_attr=graph_attr):
    h1 = Run("Horizon 1:\nClause Extraction MVP")
    h2 = Run("Horizon 2:\nAutomated Compliance Alerts")
    h3 = Run("Horizon 3:\nPredictive Risk Modeling")

    h1 >> Edge(label="Scaling", color="darkblue") >> h2 >> Edge(label="Intelligence", color="purple") >> h3