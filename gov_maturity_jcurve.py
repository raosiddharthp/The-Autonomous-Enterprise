from diagrams import Diagram, Edge
from diagrams.generic.compute import Rack
from diagrams.gcp.compute import Run

graph_attr = {"pad": "0.1", "nodesep": "1.0", "ranksep": "1.5", "bgcolor": "transparent"}

with Diagram("Outcome: Governance Maturity J-Curve", show=False, filename="gov_maturity_jcurve", direction="LR", graph_attr=graph_attr):
    start = Rack("Manual Triage\n(Baseline)")
    dip = Run("Agent Integration\n(Learning Phase)")
    surge = Run("Swarm Stabilization\n(Hyper-Productivity)")

    start >> Edge(color="red") >> dip >> Edge(color="darkgreen", style="bold") >> surge