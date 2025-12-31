from diagrams import Diagram, Edge
from diagrams.generic.blank import Blank
from diagrams.gcp.compute import GCE, Run

graph_attr = {"pad": "0.1", "nodesep": "0.8", "ranksep": "1.0", "bgcolor": "transparent"}

with Diagram("FinOps View: Cost Scaling", show=False, filename="doc_finops_spend", direction="LR", graph_attr=graph_attr):
    legacy = GCE("Traditional VM\n(Fixed Cost)")
    target = Run("Scale-to-Zero\n(Pay-per-Doc)")
    savings = Blank("60% Cost Reduction")

    legacy >> Edge(label="Migrate", color="darkred") >> target >> Edge(color="darkgreen") >> savings