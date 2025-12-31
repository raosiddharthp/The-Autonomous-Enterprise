from diagrams import Diagram, Edge
from diagrams.gcp.ml import VertexAI
from diagrams.generic.blank import Blank

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Mathematical Integrity: Pareto Curve", show=False, filename="gov_pareto_curve", direction="LR", graph_attr=graph_attr):
    model = VertexAI("Drift Monitoring")
    curve = Blank("Pareto Frontier\n(Optimal Integrity)")
    gates = Blank("Quality Gates")

    model >> Edge(label="Optimize") >> curve >> gates